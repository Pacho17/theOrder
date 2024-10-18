from rest_framework.serializers import ModelSerializer
from apps.productos.models import Producto

class ProductosSerializers(ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'