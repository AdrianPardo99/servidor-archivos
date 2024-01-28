from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    Software,
    ListarSoftwareSerializer,
    ActualizarSoftwareSerializer,
    CrearSoftwareSerializer,
    Carpeta,
    ListarCarpetaSerializer,
    CrearCarpetaSerializer,
    ActualizarCarpetaSerializer,
)
from rest.pagination import CustomPagination
from repositorio.utils import get_zip_file


class SoftwareViewSet(ModelViewSet):
    """ViewSet de interacción con el modelo de datos Software"""

    permission_classes = [IsAdminUser]
    queryset = Software.objects.filter().order_by("creacion")
    http_method_names = ["get", "patch", "post", "delete"]
    parser_classes = [MultiPartParser]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "nombre",
    ]
    ordering_fields = [
        "nombre",
    ]
    lookup_field = "pk"

    def get_serializer_class(self):
        serializers = {
            "create": CrearSoftwareSerializer,
            "list": ListarSoftwareSerializer,
            "retrieve": ListarSoftwareSerializer,
            "partial_update": ActualizarSoftwareSerializer,
            "update": ActualizarSoftwareSerializer,
        }
        return serializers.get(self.action, CrearSoftwareSerializer)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="paginate",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                required=False,
                description="Set to false to disable pagination",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("paginate") == "false":
            self.pagination_class = None  # Desactiva la paginación
        else:
            self.pagination_class = (
                CustomPagination  # Utiliza tu paginación personalizada
            )
        return super().list(request, *args, **kwargs)


class CarpetaViewSet(ModelViewSet):
    """ViewSet de interacción con el modelo de datos Carpeta"""

    permission_classes = [IsAdminUser]
    queryset = Carpeta.objects.filter().order_by("creacion")
    http_method_names = ["get", "patch", "post", "delete"]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "nombre",
    ]
    ordering_fields = [
        "nombre",
    ]
    lookup_field = "pk"

    def get_serializer_class(self):
        serializers = {
            "create": CrearCarpetaSerializer,
            "list": ListarCarpetaSerializer,
            "retrieve": ListarCarpetaSerializer,
            "partial_update": ActualizarCarpetaSerializer,
            "update": ActualizarCarpetaSerializer,
        }
        return serializers.get(self.action, CrearCarpetaSerializer)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="paginate",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                required=False,
                description="Set to false to disable pagination",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("paginate") == "false":
            self.pagination_class = None  # Desactiva la paginación
        else:
            self.pagination_class = (
                CustomPagination  # Utiliza tu paginación personalizada
            )
        return super().list(request, *args, **kwargs)


class DescargaViewSet(ModelViewSet):
    """ViewSet de interacción con el modelo de datos Carpeta y descargar los archivos que contiene la misma"""

    permission_classes = [AllowAny]
    queryset = Carpeta.objects.filter().order_by("creacion")
    http_method_names = [
        "get",
    ]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "nombre",
    ]
    ordering_fields = [
        "nombre",
    ]
    lookup_field = "pk"
    serializer_class = ListarCarpetaSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="paginate",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                required=False,
                description="Set to false to disable pagination",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("paginate") == "false":
            self.pagination_class = None  # Desactiva la paginación
        else:
            self.pagination_class = (
                CustomPagination  # Utiliza tu paginación personalizada
            )
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        temp_file = get_zip_file(instance)
        response = HttpResponse(temp_file, content_type="application/zip")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={instance.nombre}_output.zip"
        return response
