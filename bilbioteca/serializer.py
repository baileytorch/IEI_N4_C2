from rest_framework import serializers

from .models import Pais, Region, Provincia, Comuna, Direccion
from .models import Biblioteca, Autor, Genero, SubGenero, Editorial, Idioma, Edicion, Libro
from .models import Estado, Ubicacion, Inventario, Usuario, Prestamo

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('__all__')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('__all__')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('__all__')

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ('__all__')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')

class SubGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenero
        fields = ('__all__')