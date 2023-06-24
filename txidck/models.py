from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExtraBaseModel(BaseModel):
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='created_by')
    approved_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='approved_by')
    cancelled_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='cancelled_by')
    deleted_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='deleted_by')

    class Meta:
        abstract = True