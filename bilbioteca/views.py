from django.shortcuts import render
from django import forms
from rest_framework import viewsets
from django.views.generic import ListView, CreateView

from . import models as mo
from . import serializer as ser

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = mo.Pais.objects.all()
    serializer_class = ser.PaisSerializer

class PaisListView(ListView):
    model = mo.Pais
    template_name = 'biblioteca/paises/lista_paises.html'

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

class BibliotecaListView(ListView):
    model = mo.Biblioteca
    template_name = 'biblioteca/biblioteca/lista_bibliotecas.html'

class AutorListView(ListView):
    model = mo.Autor
    template_name = 'biblioteca/autor/lista_autores.html'
    
class AutorCreateView(CreateView):
    fields = ['nombre','pseudonimo','nacionalidad','fecha_nacimiento','fecha_defuncion','biografia']
    model = mo.Autor
    success_url = 'autores/listado_autores'
    template_name = 'biblioteca/autor/crear_autor.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paises'] = mo.Pais.objects.all()
        return context