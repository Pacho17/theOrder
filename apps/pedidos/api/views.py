from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedido
from apps. pedidos.api.serializers import PedidoSerializer

class PedidoModelViewset(ModelViewSet):
    serializer_class=PedidoSerializer
    queryset= Pedido.objects.all()