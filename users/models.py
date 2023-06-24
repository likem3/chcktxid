from django.db import models
from txidck.models import BaseModel


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

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    blockchain = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    wallet_id = models.CharField(unique=True, max_length=255)
    label = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nonactive')

    def __str__(self):
        return self.wallet_id
    
    class Meta:
        db_table = 'users_wallets'