from django.db import models
from django.utils import timezone

# Create your models here.


class Tienda(models.Model):
    nombre = models.CharField(max_length=30)
    nombre_sucursal = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    region = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombre)
