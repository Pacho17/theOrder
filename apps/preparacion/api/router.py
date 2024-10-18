from rest_framework.routers import DefaultRouter
from apps.preparacion.api.views import AreaPreparacionModelViewSet

router_preparacion = DefaultRouter()
router_preparacion.register(prefix="area_preparacion",basename="area_preparacion", viewset=AreaPreparacionModelViewSet)