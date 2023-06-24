from django.db import models
from txidck.models import BaseModel, ExtraBaseModel
from users.models import Account, Wallet
from payments.models import Wallet as PaymentsWallet

class Transaction(ExtraBaseModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    )

    code = models.CharField(max_length=255)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='account_transactions')
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE, related_name='wallet_transactions')
    wallet_address = models.CharField(max_length=100)
    payment_wallet = models.ForeignKey(to=PaymentsWallet, on_delete=models.CASCADE, related_name='payment_wallet_transactions')
    payment_wallet_address = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=16, decimal_places=6)
    blockchain = models.CharField(max_length=50)
    network = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cancel_reason = models.TextField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    bill_url = models.URLField(null=True, blank=True)
    proof_of_payment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.code
    
    class Meta:
        db_table = 'recharges_transaction'
