from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from .models import Reward
from .serializers import (
    RewardSerializer, 
    AddPointsSerializer, 
    RedeemPointsSerializer
)
from .exceptions import InsufficientPointsError


class RewardBalanceView(APIView):
    """
    GET: Returns the current reward balance of the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reward, created = Reward.objects.get_or_create(user=request.user)
        serializer = RewardSerializer(reward)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseCreateView(APIView):
    """
    POST: Processes a purchase and adds corresponding points to the user's reward account.
    Expected data: {"amount": <float>}
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AddPointsSerializer(data=request.data)
        if serializer.is_valid():
            reward, created = Reward.objects.get_or_create(user=request.user)
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
    POST: Redeems a specified amount of points from the user's balance.
    Expected data: {"points": <int>}
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = RedeemPointsSerializer(data=request.data)
        if serializer.is_valid():
            reward, created = Reward.objects.get_or_create(user=request.user)
            points_to_redeem = serializer.validated_data['points']
            
            try:
                reward.redeem_points(points_to_redeem)
                return Response({
                    "message": _("Points redeemed successfully."),
                    "new_balance": reward.total_points,
                    "points_redeemed": points_to_redeem
                }, status=status.HTTP_200_OK)
            except InsufficientPointsError as e:
                return Response({
                    "error": str(e),
                    "current_balance": reward.total_points
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
