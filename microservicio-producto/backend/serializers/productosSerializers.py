from rest_framework import serializers

from backend.models.productos import Productos

from backend.models.categoria import Categoria
from backend.serializers.categoriaSerializers import Categoriaserializers

class ProductosSerializers(serializers.ModelSerializer):
    #Categorias = Categoriaserializers()
    class Meta:
        model = Productos
        fields = "__all__"
        #fields =  ["id_productos","codigo","producto","imagen","stock","precio_compra","precio_venta","venta","fecha","Categorias"]
     
    """def to_representation(self, obj):
        productos = Productos.objects.get(id_productos=obj.id_productos)
        categorias = Categoria.objects.get(productos=obj.id_productos)
            
        return{
            'id_producto': productos.id_productos,
            "codigo": productos.codigo,
            "producto" : productos.producto ,
            "imagen": "https://sistema-control-inventario.herokuapp.com"+productos.imagen.url ,
            "stock": productos.stock,
            "precio_compra" : format(productos.precio_compra, ",.2f"),
            "precio_venta": format(productos.precio_venta,",.2f"),
            "venta": productos.venta,
            "fecha": format(productos.fecha,'%Y-%m-%d %H:%M:%S'),
            "Categorias":{
                "id_categoria": categorias.id_categoria,
                "categoria": categorias.categoria,
                "fecha": format(categorias.fecha,'%Y-%m-%d %H:%M:%S' )
            }
        }"""