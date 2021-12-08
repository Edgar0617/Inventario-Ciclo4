from django.db import models

class Clientes(models.Model):
    
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 100)
    documento = models.IntegerField(unique=True)
    email = models.EmailField('Email', max_length = 100)
    telefono = models.CharField('Telefono', max_length = 10)
    direccion = models.CharField('Dirección', max_length = 100)
    fecha_nacimiento = models.DateField()
    compras = models.IntegerField(default=0)
    Ultima_compra = models.DateTimeField(blank=False)
    
    def __str__(self):
        return self.nombre