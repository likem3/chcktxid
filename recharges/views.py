from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from recharges.serializers import TransactionSerializer, BillSerializer
from recharges.models import Transaction


class TransactionCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.select_related('account').all()
    serializer_class = TransactionSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        # Add any additional context data as needed
        return context


class UpdateTransactionView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.select_related('account').all()
    serializer_class = TransactionSerializer


class BillTransactionApi(APIView):
    def get(self, request, code):
        try:
            transaction = Transaction.objects.get(code=code)
            serializer = BillSerializer(transaction)

            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response(status=404)
