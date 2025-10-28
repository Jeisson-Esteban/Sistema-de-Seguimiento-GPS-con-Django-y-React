from rest_framework import generics
# Necesitamos importar permissions y AllowAny
from rest_framework import permissions 
from rest_framework.permissions import AllowAny 

from .models import Location
from .serializers import LocationSerializer

# ----------------------------------------------------
# 1. VISTA PARA CREAR/GUARDAR UBICACIONES (POST)
# ----------------------------------------------------
class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # CÓDIGO AÑADIDO: Permite que cualquier dispositivo envíe datos a esta vista.
    permission_classes = [AllowAny]

# ----------------------------------------------------
# 2. VISTA PARA LISTAR UBICACIONES (GET)
# ----------------------------------------------------
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all().order_by('session_id', 'created_at')
    serializer_class = LocationSerializer
    # CÓDIGO AÑADIDO: Permite que cualquier dispositivo reciba la lista de datos.
    permission_classes = [AllowAny]