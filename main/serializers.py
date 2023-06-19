from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.settings import CRYPTO_CURRENCIES, TOKENS


class CheckTXIDSerializer(serializers.Serializer):
    txid = serializers.CharField(required=True)
    # fromAddress = serializers.CharField(required=True)
    # toAddress = serializers.CharField(required=True)
    # amount = serializers.DecimalField(required=True)
