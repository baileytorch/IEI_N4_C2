from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    nacionalidad = models.CharField(max_length=30,null=False)
    iso_2 = models.CharField(max_length=2,null=False)
    iso_3 = models.CharField(max_length=3,null=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    pseudonimo = models.CharField(max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True)
    fecha_defuncion = models.DateField(null=True)