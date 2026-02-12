from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import Reward, RewardTransaction

class RewardTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing transaction history.
    """
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)

    class Meta:
        model = RewardTransaction
        fields = [
            'id', 
            'transaction_type', 
            'transaction_type_display', 
            'points', 
            'amount', 
            'created_at'
        ]
        read_only_fields = fields


class RewardSerializer(serializers.ModelSerializer):
    """
    Serializer to view user reward balance and recent transactions.
    """
    username = serializers.CharField(source='user.username', read_only=True)
    transactions = RewardTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Reward
        fields = ['username', 'total_points', 'updated_at', 'transactions']
        read_only_fields = fields


class AddPointsSerializer(serializers.Serializer):
    """
    Serializer for the purchase/add points endpoint.
    """
    amount = serializers.FloatField(
        required=True,
        min_value=0.01,
        help_text=_("The purchase amount to calculate points from. Must be positive.")
    )

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("The amount must be a positive number."))
        return value


class RedeemPointsSerializer(serializers.Serializer):
    """
    Serializer for the redeem points endpoint.
    """
    points = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text=_("The number of points to redeem. Must be at least 1.")
    )

    def validate_points(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("The points to redeem must be a positive integer."))
        return value
