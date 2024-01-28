from django.urls import include, path
from rest_framework_simplejwt.views import token_obtain_pair

from .repositorio.routers import router as repositorio_routers

urlpatterns = [
    path("login", token_obtain_pair, name="login"),
    path("", include(repositorio_routers.urls)),
]
