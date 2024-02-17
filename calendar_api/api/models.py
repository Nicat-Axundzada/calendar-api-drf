from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organized_events")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=250)
    guests = models.ManyToManyField(User, related_name="invited_events")

    def __str__(self):
        return self.title
