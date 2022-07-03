from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comida(models.Model):

    camada = models.IntegerField()
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"
    

class Cocinero(models.Model):
    
    camada = models.IntegerField()
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Receta(models.Model):

    camada = models.IntegerField()
    ingrediente = models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Ingredientes: {self.ingrediente}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)

