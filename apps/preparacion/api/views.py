from rest_framework.viewsets import ModelViewSet
from apps.preparacion.models import AreaPreparacion
from apps.preparacion.api.serializers import AreaPreparacionSerializer

class AreaPreparacionModelViewSet(ModelViewSet):
    serializer_class=AreaPreparacionSerializer
    queryset= AreaPreparacion.objects.all()