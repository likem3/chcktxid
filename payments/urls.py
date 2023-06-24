from django.urls import path
from payments.views import WalletListCreateView, WalletRetrieveUpdateDestroyView

urlpatterns = [
    path('payments-wallets/', WalletListCreateView.as_view(), name='wallet-list-create'),
    path('payments-wallets/<int:pk>/', WalletRetrieveUpdateDestroyView.as_view(), name='wallet-detail'),
]