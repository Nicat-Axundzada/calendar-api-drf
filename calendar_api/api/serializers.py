from rest_framework import serializers
from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "organizer", "date",
                  "start_time", "end_time", "location", "guests", "is_active"]
