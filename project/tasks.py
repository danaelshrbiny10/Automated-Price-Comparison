'''
from celery import shared_tasks
from .celery import app
from django.conf import settings
import jumiascraper


@shared_tasks
def jumiascraper():
    print("worked--------------------------")
    '''