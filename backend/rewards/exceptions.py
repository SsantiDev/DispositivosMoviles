from django.utils.translation import gettext_lazy as _

class InsufficientPointsError(Exception):
    """
    Exception raised when a user tries to redeem more points than they have in their balance.
    """
    def __init__(self, message=None, balance=None, requested=None):
        if not message:
            message = _("Insufficient points for this operation.")
        self.message = message
        self.balance = balance
        self.requested = requested
        super().__init__(self.message)

    def __str__(self):
        if self.balance is not None and self.requested is not None:
            return f"{self.message} (Balance: {self.balance}, Requested: {self.requested})"
        return self.message
