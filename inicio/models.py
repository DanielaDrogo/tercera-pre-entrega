from django.db import models

# Create your models here.
class planta(models.Model):
    tipo = models.CharField(max_length=15)
    especie = models.CharField(max_length=30)
    
    def __str__(self):
        return f'planta: {self.tipo} {self.especie}'

