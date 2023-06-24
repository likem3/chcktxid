from rest_framework import generics, parsers
from payments.models import Wallet
from payments.serializers import PaymentWalletSerializer

class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = PaymentWalletSerializer
    # parser_classes = [parsers.MultiPartParser]

class WalletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = PaymentWalletSerializer
    http_method_names = ["get", "patch"]