from api.models import Event
from api.serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
# Create your views here.


class EventAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # guests_id = request.data.get('guest_ids', [])
        guests_id = request.query_params.get('guest_ids')
        if guests_id:
            guests_id_list = [int(guest_id)
                              for guest_id in guests_id.split(',')]
            events = Event.objects.filter(
                guests__id__in=guests_id_list, is_active=True).distinct()
        elif guests_id == None:
            events = Event.objects.filter(is_active=True)
        else:
            events = []
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk, is_active=True)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.is_active = False
        event.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
