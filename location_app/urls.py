from django.urls import path
from .views import LocationCreateView, LocationListView

urlpatterns = [
    path('location/', LocationCreateView.as_view(), name='location-create'),
    path('locations/', LocationListView.as_view(), name='location-list'),
]