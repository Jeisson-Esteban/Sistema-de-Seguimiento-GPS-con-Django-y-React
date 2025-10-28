from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer

class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all().order_by('session_id', 'created_at')
    serializer_class = LocationSerializer