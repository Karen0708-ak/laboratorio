from django.db import models

class Vinedo(models.Model):
    id_libro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    propietario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
