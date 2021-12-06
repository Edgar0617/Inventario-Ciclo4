from rest_framework import serializers, viewsets

from backend.models.categoria import Categoria
from backend.serializers.categoriaSerializers import Categoriaserializers

class CategoriaCreateView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id_categoria')
    serializer_class = Categoriaserializers
    
