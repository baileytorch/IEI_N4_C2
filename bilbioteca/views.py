from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView

from . import models as mo
from . import serializer as ser

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = mo.Pais.objects.all()
    serializer_class = ser.PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = mo.Region.objects.all()
    serializer_class = ser.RegionSerializer

class RegionListView(ListView):
    model = mo.Region
    template_name = 'biblioteca/regiones/lista_regiones.html'

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = mo.Provincia.objects.all()
    serializer_class = ser.ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = mo.Comuna.objects.all()
    serializer_class = ser.ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = mo.Direccion.objects.all()
    serializer_class = ser.DireccionSerializer