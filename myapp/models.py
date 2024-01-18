# Create your models here.
# myapp/models.py

from django.db import models
from django.conf import settings

class Maquina(models.Model):
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    no_serie = models.CharField(max_length=100, unique=True)
    observaciones = models.TextField()

    def __str__ (self):
            return f"{self.marca} {self.modelo} {self.no_serie}"

class Prestamo(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    