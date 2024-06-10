import os

from news_portal_service import settings
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_portal_service.settings")
app = Celery(
    "library_service",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.config_from_object("django.conf:settings")

app.autodiscover_tasks(packages=["fresh_news.periodic_tasks"])
