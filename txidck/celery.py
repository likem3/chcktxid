import os
from celery import Celery
from txidck.settings import CELERY_BEAT_SCHEDULE
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'txidck.settings')

app = Celery('txidck')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
