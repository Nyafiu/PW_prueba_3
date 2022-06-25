from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Informacion(models.Model):
    nombre=models.CharField(max_length=30)
    apparteno=models.CharField(max_length=30)
    apmaterno=models.CharField(max_length=30)
    rut=models.CharField(max_length=30)
    edad=models.CharField(max_length=30)
    nombre_vacuna=models.CharField(max_length=30)
    fecha=models.DateField()