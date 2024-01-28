from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import debug_toolbar

# Endpoint for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion Swagger para Servidor de Archivos",
        default_version="v1",
        description="Documentacion de Backend para Servidor de Archivos",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Carpeta rest
    path("api/v1/", include(("rest.urls", "rest"), namespace="api")),
    # Path de API de Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger/api/v1/user/login/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="rest_framework_login",
    ),
    path(
        "swagger/api/v1/user/logout/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="rest_framework_logout",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
