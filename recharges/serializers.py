from rest_framework import serializers
from recharges.models import Transaction
from users.models import Account, Wallet as AccountWallet
from payments.models import Wallet as PaymentWallet
from payments.settings import BLOCKCHAIN_OPTIONS, NETWORK_OPTIONS, BLOCKCHAIN_CODE, NETWORK_CODE
import time
from django.utils import timezone
from datetime import timedelta


class TransactionSerializer(serializers.ModelSerializer):
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.filter(status='active'), source='account', many=False)
    blockchain = serializers.ChoiceField(choices=BLOCKCHAIN_OPTIONS)
    network = serializers.ChoiceField(choices=NETWORK_OPTIONS)
    amount = serializers.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        model = Transaction
        fields = [
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
            'code',
            'wallet_address',
            'payment_wallet_address',
            'status',
            'cancel_reason',
            'approved_by',
            'cancelled_by',
            'created_by',
            'deleted_by',
            'payment_wallet_id',
            'wallet_id',
            'blockchain',
            'network',
            'amount',
            'account_id',
            'expired_at',
            'proof_of_payment',
            'bill_url'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
            'code',
            'wallet_address',
            'payment_wallet_address',
            'status',
            'cancel_reason',
            'approved_by',
            'cancelled_by',
            'created_by',
            'deleted_by',
            'payment_wallet_id',
            'wallet_id',
            'expired_at',
            'proof_of_payment',
            'bill_url'
        ]
          
    def create(self, validated_data):
        account = validated_data.pop('account')
        blockchain = validated_data['blockchain']
        network = validated_data['network']
        
        request = self.context.get('request')
        host_url = request.build_absolute_uri('/')

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
                account=account,
                wallet=account_wallet,
                wallet_address=account_wallet.address,
                payment_wallet=payment_wallet,
                payment_wallet_address=payment_wallet.address,
                amount=validated_data['amount'],
                blockchain=blockchain,
                network=network,
                status='pending',
                expired_at=(timezone.now() + timedelta(minutes=30)),
                bill_url=f'{host_url}bill/{trx_code}/'
            )

            return trx

        except Exception as e:
            raise Exception(f'Failed when create transaction {e}')


class BillSerializer(serializers.Serializer):
    code = serializers.CharField()
    created_at = serializers.DateTimeField()
    expired_at = serializers.DateTimeField()
    amount = serializers.DecimalField(max_digits=16, decimal_places=6)
    network = serializers.CharField()
    blockchain = serializers.CharField()
    from_address = serializers.CharField(source='wallet_address')
    to_address = serializers.CharField(source='payment_wallet_address')
    to_address_qr = serializers.CharField(source='payment_wallet.qr_b64')
    # bill_url = serializers.CharField()

    def to_representation(self, instance):
        current_time = timezone.now()
        if instance.expired_at < current_time:
            return {'message': 'Transaction has expired'}
        return super().to_representation(instance)
    

class DepositWalletSerializer(serializers.Serializer):
    account_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.filter(status='active'), source='account', many=False)
    blockchain = serializers.ChoiceField(choices=BLOCKCHAIN_OPTIONS)
    network = serializers.ChoiceField(choices=NETWORK_OPTIONS)

    def create(self, validated_data):
        account = validated_data.pop('account')
        blockchain = validated_data['blockchain']
        network = validated_data['network']
        
        try:
            account_wallet = AccountWallet.objects.get(account=account, blockchain=blockchain, network=network)

        except AccountWallet.DoesNotExist:
            account_wallet = AccountWallet.create_user_wallet(
                account=account,
                user_id=account.user_id,
                blockchain=blockchain,
                network=network
            )

        return account_wallet
        