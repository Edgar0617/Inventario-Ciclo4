from rest_framework import viewsets
from backend.models.productos import Productos
from backend.models.categoria import Categoria
from backend.serializers.productosSerializers import ProductosSerializers

from backend.serializers.categoriaSerializers import Categoriaserializers


class ProductoCreateView(viewsets.ModelViewSet):
    queryset = Productos.objects.all().order_by('id_productos')
    serializer_class = ProductosSerializers 
    
   