from django.db import models
from txidck.models import BaseModel
from payments.cryptoapi.address import CreateAddressHandler

class Account(BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('nonactive', 'Non-active'),
        ('suspended', 'Suspended'),
    )

    uuid = models.UUIDField(unique=True, editable=False)
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nonactive')

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users_accounts'


class Wallet(BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('nonactive', 'Non-Active'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='wallets')
    user_id = models.IntegerField()
    blockchain = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    address = models.CharField(unique=True, max_length=255)
    label = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nonactive')

    def __str__(self):
        return self.address
    
    class Meta:
        db_table = 'users_wallets'

    @classmethod
    def create_user_wallet(cls, account, user_id, blockchain, network):
        handler = CreateAddressHandler()
        # handler.create_address(blockchain=validated_data['blockchain'], network=validated_data['network'], label=account.user_id)
        handler.create_fake_adress(blockchain=blockchain, network=network, label=account.user_id)

        if handler._address and handler._label:
            wallet = cls.objects.create(
                account=account,
                user_id=user_id,
                blockchain=blockchain,
                network=network,
                address=handler._address,
                label=handler._label,
                status='active'
            )

            return wallet
        else:
            return
    
    @classmethod
    def get_account_blockchain_wallet(cls, account, blockchain, network):
        return cls.objects.filter(
            account=account,
            blockchain=blockchain,
            network=network
        )