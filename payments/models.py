from django.db import models
from txidck.models import BaseModel

class Wallet(BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('nonactive', 'Non-Active'),
    )

    blockchain = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    address = models.CharField(unique=True, max_length=255)
    label = models.CharField(unique=True, max_length=255)
    qr_b64 = models.TextField(blank=True, null=True)
    icon_url = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return self.label
    
    class Meta:
        db_table = 'payments_wallets'
