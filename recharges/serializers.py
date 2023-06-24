from rest_framework import serializers
from recharges.models import Transaction
from users.models import Account, Wallet as AccountWallet
from payments.models import Wallet as PaymentWallet
from payments.settings import BLOCKCHAIN_OPTIONS, NETWORK_OPTIONS, BLOCKCHAIN_CODE, NETWORK_CODE
import time
from datetime import datetime

class CreateTransactionSerializer(serializers.Serializer):
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.filter(status='active'), source='account', many=False)
    blockchain = serializers.ChoiceField(choices=BLOCKCHAIN_OPTIONS)
    network = serializers.ChoiceField(choices=NETWORK_OPTIONS)
    amount = serializers.DecimalField(max_digits=16, decimal_places=6)

    def validate(self, attrs):
        if not PaymentWallet.objects.filter(blockchain=attrs['blockchain'], network=attrs['network'], status='active').exists():
            raise serializers.ValidationError('No Payment Wallet active for this blockchain or network')

        return attrs
            
    def create(self, validated_data):
        account = validated_data.pop('account')
        blockchain = validated_data['blockchain']
        network = validated_data['network']

        account_wallet = account.wallets.filter(blockchain=blockchain, network=network).first()

        try:
            payment_wallet = PaymentWallet.objects.filter(blockchain=blockchain, network=network, status='active').first()
            if not payment_wallet:
                raise Exception("No Payment Wallet active for this blockchain or network")

            if not account_wallet:
                account_wallet = AccountWallet.create_user_wallet(
                    account=account,
                    user_id=account.user_id,
                    blockchain=blockchain,
                    network=network
                )
            cc_code = BLOCKCHAIN_CODE[blockchain]
            net_code = NETWORK_CODE[network]
            trx_code = f'{cc_code}{net_code}{account.user_id}-{int(time.time())}'
            trx = Transaction.objects.create(
                code=trx_code,
                account_id=account,
                wallet_id=account_wallet,
                wallet_address=account_wallet.address,
                payment_wallet_id=payment_wallet,
                payment_wallet_address=payment_wallet.address,
                amount=validated_data['amount'],
                blockchain=blockchain,
                network=network,
                status='pending'
            )

            return trx

        except Exception as e:
            raise Exception(f'Failed when create transaction {e}')
        # return super().create(validated_data)