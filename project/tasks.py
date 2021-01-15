from celery import shared_tasks
from django.conf import settings
import jumiascraper


@shared_tasks
def jumiascraper():
    print("worked--------------------------")