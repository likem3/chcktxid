from django.urls import path
from recharges.views import TransactionCreateView, BillTransactionApi

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('bill/<str:code>/', BillTransactionApi.as_view(), name='bill-detail'),
]