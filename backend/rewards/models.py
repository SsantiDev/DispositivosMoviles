from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .exceptions import InsufficientPointsError


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
        validators=[MinValueValidator(0)],
        verbose_name=_("Total Points")
    )

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_points(self, amount: float) -> None:
        """
        Calculates points based on the purchase amount, adds them to the balance,
        and records the transaction.
        Calculation: amount / 1000 (integer division).
        """
        if amount < 0:
            raise ValueError(_("Amount cannot be negative."))
            
        earned_points = int(amount // self.POINTS_PER_CURRENCY_UNIT)
        if earned_points > 0:
            self.total_points += earned_points
            self.save()
            # Record transaction
            RewardTransaction.objects.create(
                reward=self,
                transaction_type=RewardTransaction.Types.EARNED,
                points=earned_points,
                amount=amount
            )

    def redeem_points(self, points_to_redeem: int) -> None:
        """
        Subtracts points from the balance if sufficient and records the transaction.
        Raises InsufficientPointsError if the balance is too low.
        """
        if points_to_redeem < 0:
            raise ValueError(_("Points to redeem cannot be negative."))
            
        if points_to_redeem > self.total_points:
            raise InsufficientPointsError(
                balance=self.total_points,
                requested=points_to_redeem
            )
        
        self.total_points -= points_to_redeem
        self.save()
        # Record transaction
        RewardTransaction.objects.create(
            reward=self,
            transaction_type=RewardTransaction.Types.REDEEMED,
            points=points_to_redeem,
            amount=points_to_redeem * self.VALUE_PER_POINT
        )

    def __str__(self):
        return f"Reward for {self.user.username} - Balance: {self.total_points}"

    class Meta:
        verbose_name = _("Reward")
        verbose_name_plural = _("Rewards")


class RewardTransaction(models.Model):
    """
    Audit log for point EARNED or REDEEMED events.
    """
    class Types(models.TextChoices):
        EARNED = 'EARNED', _('Earned')
        REDEEMED = 'REDEEMED', _('Redeemed')

    reward = models.ForeignKey(
        Reward,
        on_delete=models.CASCADE,
        related_name='transactions',
        null=False,
        blank=False
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=Types.choices,
        null=False,
        blank=False,
        verbose_name=_("Transaction Type")
    )
    points = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        verbose_name=_("Points")
    )
    amount = models.DecimalField(
        max_length=15,
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name=_("Reference Amount")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Transaction Date"))

    def save(self, *args, **kwargs):
        """
        Validation to ensure redemption doesn't exceed current balance.
        Note: Reward.redeem_points already checks this, but this is a safety net.
        Only applies on creation.
        """
        if not self.pk and self.transaction_type == self.Types.REDEEMED:
            if self.points > self.reward.total_points:
                raise ValidationError(
                    _("Cannot redeem %(points)s points. Current balance is %(balance)s."),
                    params={'points': self.points, 'balance': self.reward.total_points},
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_type} - {self.points} pts for {self.reward.user.username}"

    class Meta:
        verbose_name = _("Reward Transaction")
        verbose_name_plural = _("Reward Transactions")
        ordering = ['-created_at']
