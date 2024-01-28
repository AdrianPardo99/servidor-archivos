from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    prefix="software",
    viewset=views.SoftwareViewSet,
    basename="software",
)

router.register(
    prefix="carpeta",
    viewset=views.CarpetaViewSet,
    basename="carpeta",
)
