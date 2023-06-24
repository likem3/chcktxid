from rest_framework import generics
from recharges.serializers import CreateTransactionSerializer

class TransactionCreateView(generics.CreateAPIView):
    serializer_class = CreateTransactionSerializer