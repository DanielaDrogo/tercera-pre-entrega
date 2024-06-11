from django.db import models

# Create your models here.

class planta(models.Model):
    tipo = models.CharField(max_length=15)
    especie = models.CharField(max_length=30)
