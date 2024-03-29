from django.urls import path
from api.views import EventAPIView, EventDetailAPIView, CreateUserView

app_name = "api"

urlpatterns = [
    path("event/", EventAPIView.as_view()),
    path("event/detail/<int:pk>", EventDetailAPIView.as_view()),
    path('users/', CreateUserView.as_view()),
]
