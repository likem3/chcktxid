from django.db import models
from txidck.models import BaseModel, ExtraBaseModel
from users.models import Account, Wallet as AccountWallet

class Wallet(BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('nonactive', 'Non-Active'),
    )

    blockchain = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    wallet_id = models.CharField(unique=True, max_length=255)
    label = models.CharField(unique=True, max_length=255)
    qr_b64 = models.TextField(blank=True, null=True)
    icon_url = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return self.label
    
    class Meta:
        db_table = 'payments_wallets'


# class Recharge(ExtraBaseModel):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('completed', 'Completed'),
#         ('failed', 'Failed'),
#         ('cancelled', 'Cancelled'),
#     )

#     account_id = models.ForeignKey(to=Account, on_delete=models.CASCADE)
#     wallet_id = models.ForeignKey(to=AccountWallet, on_delete=models.CASCADE, related_name='account_wallet')
#     wallet_address = models.CharField(max_length=100)
#     payment_wallet_id = models.ForeignKey(to=Wallet, on_delete=models.CASCADE)
#     payment_wallet_address = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=16, decimal_places=6)
#     blockchain = models.CharField(max_length=50)
#     network = models.CharField(max_length=30)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     cancel_reason = models.TextField(null=True, blank=True)