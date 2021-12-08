from django.contrib import admin

# Register your models here.

from .models.clientes import  Clientes

admin.site.register(Clientes)

