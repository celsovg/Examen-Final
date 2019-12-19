from django.db import models
from django.utils import timezone 



class RegistroUsuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


