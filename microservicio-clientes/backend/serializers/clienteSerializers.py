from rest_framework import serializers
from backend.models.clientes import Clientes

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
    def to_representation(self, obj):
        clientes = Clientes.objects.get(id_cliente=obj.id_cliente)
        return{
            "id_cliente": clientes.id_cliente,
            "nombre": clientes.nombre,
            "documento": format(clientes.documento,',.0f'),
            "email": clientes.email,
            "telefono": clientes.telefono,
            "direccion": clientes.direccion,
            "fecha_nacimiento": clientes.fecha_nacimiento,
            "compras": clientes.compras,
            "Ultima_compra":format(clientes.Ultima_compra,'%Y-%m-%d %H:%M:%S')
        }