from rest_framework import serializers
from backend.models.categoria import Categoria

class Categoriaserializers(serializers.ModelSerializer):
   class Meta:
      model = Categoria
      fields = '__all__'
      
   def to_representation(self, obj):
      categorias = Categoria.objects.get(id_categoria=obj.id_categoria)
      return{
         "id_categoria": categorias.id_categoria,
         "categoria": categorias.categoria,
         "fecha": format(categorias.fecha, '%Y-%m-%d %H:%M:%S')
      }