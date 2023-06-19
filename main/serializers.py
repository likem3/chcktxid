from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.settings import CRYPTO_CURRENCIES, TOKENS


class CheckTXIDSerializer(serializers.Serializer):
    txid = serializers.CharField(required=True)
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.DecimalField(required=True, max_digits=12, decimal_places=6)
