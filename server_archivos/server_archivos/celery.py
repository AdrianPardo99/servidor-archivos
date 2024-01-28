import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_archivos.settings")

app = Celery("server_archivos")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
