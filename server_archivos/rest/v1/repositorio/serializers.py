from django.contrib.auth.models import AnonymousUser

from rest_framework import serializers

from repositorio.models import Software, Carpeta


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = [
            "nombre",
            "documento",
        ]


class ListarSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = ["pk"] + SoftwareSerializer.Meta.fields


class CrearSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = SoftwareSerializer.Meta.fields


class ActualizarSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = ("documento",)


class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = [
            "nombre",
            "archivos",
        ]


class ListarCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = ["pk"] + CarpetaSerializer.Meta.fields

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["archivos"] = []
        print(dir(instance.archivos))
        for archivo in instance.archivos.all():
            rep["archivos"].append(str(archivo))
        return rep


class CrearCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = CarpetaSerializer.Meta.fields


class ActualizarCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = ("archivos",)
