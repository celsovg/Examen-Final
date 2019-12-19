from django.db import models
from django.utils import timezone
from apps.usuario.models import RegistroUsuario
from apps.tienda.models import Tienda


class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    costo_real = models.IntegerField()
    costo_presupuestado = models.IntegerField()
    tienda = models.ForeignKey(Tienda,null=True, blank=True, on_delete=models.CASCADE)
    notas = models.TextField(null=True, blank=True)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.nombre)


class ListaDeCompras (models.Model):
    nombre_lista = models.CharField(max_length=80, null=True, blank=True)
    creador = models.ForeignKey(RegistroUsuario, null=True, blank=True, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    cantidad_productos = models.IntegerField(null=True, blank=True)
    cantidad_comprados = models.IntegerField(null=True, blank=True)
    presupuesto_total = models.IntegerField(null=True, blank=True)
    total_final = models.IntegerField(null=True, blank=True)
