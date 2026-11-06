from django.shortcuts import render
from django import forms
from rest_framework import viewsets
from django.views.generic import ListView, CreateView

from . import models as mo
from . import serializer as ser
from . import forms as fo

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
    form_class = fo.AutorForm
    model = mo.Autor
    success_url = 'listado_autores'
    template_name = 'biblioteca/autor/crear_autor.html'

class LibroListView(ListView):
    model = mo.Libro
    template_name = 'biblioteca/libro/lista_libros.html'
    
class LibroCreateView(CreateView):
    form_class = fo.LibroForm
    model = mo.Libro
    success_url = 'listado_libros'
    template_name = 'biblioteca/libro/crear_libro.html'