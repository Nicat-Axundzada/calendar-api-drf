import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calendar_api.settings')

app = Celery("calendar_api")
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def add():
    return


app.autodiscover_tasks()
