import os

from celery.schedules import crontab
from news_portal_service import settings
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_portal_service.settings")
app = Celery(
    "news_portal_service",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.config_from_object("django.conf:settings")

app.autodiscover_tasks(packages=["fresh_news.periodic_tasks"])


app.conf.beat_schedule = {
    "periodic parsing gizmochina_links": {
        "task": "fresh_news.periodic_tasks.periodic_parsing_gizmochina_links",
        "schedule": crontab(hour="1", minute="10"),
    },
    "periodic parsing popsci links": {
        "task": "fresh_news.periodic_tasks.periodic_parsing_popsci_com_links",
        "schedule": crontab(hour="1", minute="10"),
    }
}
