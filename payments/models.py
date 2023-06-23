from django.db import models
from txidck.models import BaseModel

class User(BaseModel):
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