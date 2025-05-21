from django.db import models

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    propietario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
