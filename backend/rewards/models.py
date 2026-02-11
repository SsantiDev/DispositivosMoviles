from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InsufficientPointsError(Exception):
    """Exception raised when a user tries to redeem more points than they have."""
    pass


class Reward(models.Model):
    """
    Represents the loyalty points balance for a user.
    """
    # Business logic constants
    POINTS_PER_CURRENCY_UNIT = 1000  # 1 point for every $1,000 pesos
    VALUE_PER_POINT = 100          # 1 point is worth $100 pesos

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='reward'
    )
    total_points = models.IntegerField(
        default=0,
        verbose_name="Total Points"
    )

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_points(self, amount: float) -> None:
        """
        Calculates points based on the purchase amount and adds them to the balance.
        Calculation: amount / 1000 (integer division).
        """
        earned_points = int(amount // self.POINTS_PER_CURRENCY_UNIT)
        if earned_points > 0:
            self.total_points += earned_points
            self.save()

    def redeem_points(self, points_to_redeem: int) -> None:
        """
        Subtracts points from the balance if sufficient.
        Raises InsufficientPointsError if the balance is too low.
        """
        if points_to_redeem > self.total_points:
            raise InsufficientPointsError(
                f"Insufficient points. Balance: {self.total_points}, "
                f"Requested: {points_to_redeem}"
            )
        
        self.total_points -= points_to_redeem
        self.save()

    def __str__(self):
        return f"Reward for {self.user.username} - Balance: {self.total_points}"

    class Meta:
        verbose_name = "Reward"
        verbose_name_plural = "Rewards"
