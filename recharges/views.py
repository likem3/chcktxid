from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from recharges.serializers import TransactionSerializer, BillSerializer, DepositWalletSerializer
from recharges.models import Transaction
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


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


class InitiateTransactionView(APIView):
    @swagger_auto_schema(request_body=DepositWalletSerializer)
    def post(self, request):
        serializer = DepositWalletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        deposit_wallet = serializer.save()
        wallet_data = {
            'blockchain': deposit_wallet.blockchain,
            'network': deposit_wallet.network,
            'address': deposit_wallet.address,
            'label': deposit_wallet.label, 
            'attributs': {
                'address_qr': deposit_wallet.attributs.address_qr,
                'logo': deposit_wallet.attributs.logo,
                'symbol': deposit_wallet.attributs.symbol
            }
        }

        return Response(wallet_data, status=status.HTTP_201_CREATED)
