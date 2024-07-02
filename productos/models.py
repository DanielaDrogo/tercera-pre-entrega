from django.db import models

# Create your models here.


class Maceta(models.Model):
    tamanio = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def __str__(self):
        return f'{self.tamanio} {self.material} {self.precio}' 
