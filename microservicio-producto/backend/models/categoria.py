from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField('Categoria', max_length = 100, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.categoria