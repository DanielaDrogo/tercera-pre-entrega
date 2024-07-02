from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagen_blog', blank=True, null=True)
    
    def __str__(self):
        return f'{self.titulo} {self.subtitulo} {self.cuerpo} {self.fecha} {self.imagen}'
