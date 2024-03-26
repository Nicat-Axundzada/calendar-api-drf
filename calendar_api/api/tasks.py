from celery import shared_task
from django.utils import timezone
from api.models import Event


@shared_task
def cleanup_expired_events():
    """ Delete tasks from 5 years ago.  """

    # Get the current year
    current_year = timezone.now().year

    expired_events = Event.objects.filter(end_time__lte=current_year-5)
    expired_events.delete()


@shared_task
def cleanup_inactive_events():
    """ Delete inactive tasks. """
    inactive_tasks = Event.objects.filter(is_active=False)
    inactive_tasks.delete()
