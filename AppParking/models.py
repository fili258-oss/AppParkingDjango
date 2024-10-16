from django.db import models

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=100,blank=False,null=False,unique=True)
    nit = models.IntegerField()
    direccion = models.CharField(max_length=100,blank=False,null=False)
    telefono = models.CharField(max_length=10,blank=False,null=False)
