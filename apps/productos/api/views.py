from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Producto
from apps.productos.api.serializer import ProductosSerializers

class ProductosModelsViewSet(ModelViewSet):
    serializer_class=ProductosSerializers
    queryset= Producto.objects.all()