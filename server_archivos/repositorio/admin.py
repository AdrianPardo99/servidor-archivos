from django.contrib import admin
from .models import Software, Carpeta


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "documento",
        "activo",
        "creacion",
    )
    readonly_fields = ("activo",)


@admin.register(Carpeta)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "activo",
        "creacion",
    )
    readonly_fields = ("activo",)
