from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Reward
from .serializers import (
    RewardSerializer, 
    AddPointsSerializer, 
    RedeemPointsSerializer
)
from .exceptions import InsufficientPointsError


def get_development_user(request):
    """
    Helper to return the authenticated user or a fallback user for development.
    """
    if request.user.is_authenticated:
        return request.user
    
    # Fallback to the first available user for development purposes
    user = User.objects.first()
    if not user:
        # Create a default admin user if the database is empty
        user = User.objects.create_superuser(
            username='admin', 
            email='admin@example.com', 
            password='adminpassword'
        )
    return user


class RewardBalanceView(APIView):
    """
    GET: Returns the current reward balance.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = get_development_user(request)
        reward, created = Reward.objects.get_or_create(user=user)
        serializer = RewardSerializer(reward)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseCreateView(APIView):
    """
    POST: Processes a purchase and adds corresponding points.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AddPointsSerializer(data=request.data)
        if serializer.is_valid():
            user = get_development_user(request)
            reward, created = Reward.objects.get_or_create(user=user)
            amount = serializer.validated_data['amount']
            
            reward.add_points(amount)
            
            return Response({
                "message": _("Points added successfully."),
                "new_balance": reward.total_points,
                "amount_processed": amount
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedeemPointsView(APIView):
    """
    POST: Redeems a specified amount of points.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RedeemPointsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = get_development_user(request)
        reward, created = Reward.objects.get_or_create(user=user)
        points_to_redeem = serializer.validated_data['points']
        
        try:
            reward.redeem_points(points_to_redeem)
            return Response({
                "message": _("Points redeemed successfully."),
                "new_balance": reward.total_points,
                "points_redeemed": points_to_redeem
            }, status=status.HTTP_200_OK)
        except InsufficientPointsError as e:
            from rest_framework.exceptions import ValidationError as DRFValidationError
            raise DRFValidationError(detail=str(e), code="insufficient_points")
