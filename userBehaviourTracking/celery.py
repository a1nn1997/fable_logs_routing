import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userBehaviourTracking.settings')

app = Celery('userBehaviourTracking', include=['logTracking.tasks'])

# Configure Celery using Django settings.
app.config_from_object(settings, namespace='CELERY')

# Discover tasks modules in Django apps.
app.autodiscover_tasks()
