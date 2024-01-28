from django.urls import include, path

urlpatterns = [
    path("", include(("rest.v1.urls", "rest"), namespace="v1")),
]
