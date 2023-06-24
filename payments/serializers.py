from rest_framework import serializers
from payments.models import Wallet
from payments.settings import BLOCKCHAIN_OPTIONS, NETWORK_OPTIONS
from utils.image_handler import generate_qrcode_with_logo
from payments.settings import LOGO_SETTINGS


class PaymentWalletSerializer(serializers.ModelSerializer):
    blockchain = serializers.ChoiceField(choices=BLOCKCHAIN_OPTIONS)
    network = serializers.ChoiceField(choices=NETWORK_OPTIONS)

    class Meta:
        model = Wallet
        fields = ('id', 'blockchain', 'network', 'address', 'label', 'status', 'qr_b64', 'icon_url')
        read_only_fields = ('id', 'qr_b64', 'icon_url')

    def create(self, validated_data):
        icon_url = LOGO_SETTINGS[validated_data['blockchain']]
        qr_b64 = generate_qrcode_with_logo(text=validated_data['address'], logo_path=icon_url)
        # breakpoint()
        wallet = Wallet.objects.create(icon_url=icon_url, qr_b64=qr_b64, **validated_data)
        return wallet

        