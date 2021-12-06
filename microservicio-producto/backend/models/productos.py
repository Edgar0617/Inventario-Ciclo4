from django.db import models
from .categoria import Categoria

class Productos(models.Model):
    
    
    def productos_directory_path(instance,filename):
        return 'productos/{0}'.format(filename)
    
    id_productos = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.IntegerField(default=0)
    producto = models.CharField('producto', max_length = 100)
    stock = models.IntegerField(default=0)
    precio_compra = models.DecimalField(max_digits=10,decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        
        return self.producto