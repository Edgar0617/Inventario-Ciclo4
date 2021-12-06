from django.contrib import admin
# Register your models here.

from .models.categoria import Categoria
from .models.productos import  Productos

admin.site.register(Categoria)
admin.site.register(Productos)

