from django.contrib import admin
from .models import Software, Carpeta, Compendio


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "documento",
        "activo",
        "creacion",
    )
    readonly_fields = ("activo",)


@admin.register(Carpeta)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "activo",
        "creacion",
    )
    readonly_fields = ("activo",)


@admin.register(Compendio)
class CompendioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "cantidad",
        "hash",
        "carpeta",
        "creacion",
        "actualizado",
    )
    readonly_fields = (
        "nombre",
        "archivo",
        "cantidad",
        "hash",
        "carpeta",
    )
