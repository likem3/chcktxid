from django.urls import path
from recharges.views import TransactionCreateView, BillTransactionApi, InitiateTransactionView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('bill/<str:code>/', BillTransactionApi.as_view(), name='bill-detail'),
    path('deposit-wallet/', InitiateTransactionView.as_view(), name='deposit-wallet'),
]