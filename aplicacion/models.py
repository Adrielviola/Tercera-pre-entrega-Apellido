from django.db import models

# Create your models here.
class notebook(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    emai=models.EmailField()

class Desktop(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    emai=models.EmailField()

class aio(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    emai=models.EmailField()

class celulares(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    imai=models.DecimalField(max_digits=20, decimal_places=0)
    
