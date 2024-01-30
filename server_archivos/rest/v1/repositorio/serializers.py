from rest_framework import serializers

from repositorio.models import Software, Carpeta, Compendio


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = [
            "nombre",
            "documento",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["id"] = instance.id
        return rep


class ListarSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = ["id"] + SoftwareSerializer.Meta.fields


class CrearSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = SoftwareSerializer.Meta.fields


class ActualizarSoftwareSerializer(SoftwareSerializer):
    class Meta(SoftwareSerializer.Meta):
        model = SoftwareSerializer.Meta.model
        fields = ("documento",)


class CarpetaSerializer(serializers.ModelSerializer):
    archivos = ListarSoftwareSerializer(many=True)

    class Meta:
        model = Carpeta
        fields = [
            "nombre",
            "archivos",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["id"] = instance.id
        return rep


class ListarCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = ["id"] + CarpetaSerializer.Meta.fields


class CrearCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = CarpetaSerializer.Meta.fields


class ActualizarCarpetaSerializer(CarpetaSerializer):
    class Meta(CarpetaSerializer.Meta):
        model = CarpetaSerializer.Meta.model
        fields = ("archivos",)


class CompendioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compendio
        fields = [
            "nombre",
            "cantidad",
            "hash",
            "creacion",
            "actualizado",
        ]


class ListarCompendioSerializer(CompendioSerializer):
    download_url = serializers.FileField(source="archivo")

    class Meta(CompendioSerializer.Meta):
        model = CompendioSerializer.Meta.model
        fields = ["download_url"] + CompendioSerializer.Meta.fields


class SoftwareHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = (
            "id",
            "nombre",
            "documento",
            "creacion",
            "actualizado",
        )


class CarpetaHashSerializer(serializers.ModelSerializer):
    archivos = SoftwareHashSerializer(many=True)

    class Meta:
        model = Carpeta
        fields = (
            "id",
            "nombre",
            "archivos",
            "creacion",
        )
