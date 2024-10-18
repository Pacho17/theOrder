from rest_framework.serializers import ModelSerializer
from apps.preparacion.models import AreaPreparacion

class AreaPreparacionSerializer(ModelSerializer):
    class Meta:
        model = AreaPreparacion
        fields = '__all__'