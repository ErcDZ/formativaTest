from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_ingreso = models.DateField()

    def __str__(self) -> str:
        return self.nombre

class Reparacion(models.Model):
    nombre_coche = models.CharField(max_length=100, unique=True)
    fecha_registrado = models.DateField()
    monto = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.nombre_coche