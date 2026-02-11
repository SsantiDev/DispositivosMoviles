from django.urls import path
from .views import (
    RewardBalanceView, 
    PurchaseCreateView, 
    RedeemPointsView
)

urlpatterns = [
    path('balance/', RewardBalanceView.as_view(), name='reward-balance'),
    path('purchase/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('redeem/', RedeemPointsView.as_view(), name='redeem-points'),
]
