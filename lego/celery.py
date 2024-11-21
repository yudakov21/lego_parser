import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lego.settings')
 
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@worker_ready.connect
def at_start(sender, **kwargs):
    from services.tasks import scrape_lego_sales
    scrape_lego_sales.delay()