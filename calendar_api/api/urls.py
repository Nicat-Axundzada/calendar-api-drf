from django.urls import path
from api.views import EventView, EventDetailView

urlpatterns = [
    path("event/", EventView.as_view(), name="event_list"),
    path("event/<int:pk>", EventDetailView.as_view(), name="event_detail"),
]
