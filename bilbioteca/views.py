from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais
from .models import Region
from .models import Provincia
from .models import Comuna
from .models import Direccion
from .models import Biblioteca
from .models import Autor
from .models import Genero
from .models import SubGenero
from .models import Editorial
from .models import Idioma
from .models import Edicion
from .models import Libro
from .models import Estado
from .models import Ubicacion
from .models import Inventario
from .models import Usuario
from .models import Prestamo

from .serializer import PaisSerializer
from .serializer import RegionSerializer
from .serializer import ProvinciaSerializer
from .serializer import ComunaSerializer

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer