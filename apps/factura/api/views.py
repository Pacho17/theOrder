from rest_framework.viewsets import ModelViewSet
from apps.factura.models import Factura
from apps.factura.api.serializers import FacturaSerializer

class FacturaModelViewset(ModelViewSet):
    serializer_class= FacturaSerializer
    queryset = Factura.objects.all()