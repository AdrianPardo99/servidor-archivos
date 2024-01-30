import hashlib
import json

from django.core.files import File

from celery import shared_task

from .models import Carpeta, Compendio
from .utils import get_zip_file
from rest.v1.repositorio.serializers import CarpetaHashSerializer


@shared_task
def create_and_save_zip(carpeta_id):
    instance = Carpeta.objects.get(pk=carpeta_id)
    json_data = json.dumps(
        CarpetaHashSerializer(instance=instance).data, sort_keys=True
    )
    hash_data = hashlib.sha256(json_data.encode()).hexdigest()
    print(f"Hash json: {hash_data}")
    compendio_obj = Compendio.objects.filter(carpeta=instance)
    filename = f"{instance.nombre}_output.zip"
    create = True
    if compendio_obj:
        compendio_obj = compendio_obj.first()
        print(f"Hash de compendio: {compendio_obj.hash}")
        if compendio_obj.hash == hash_data:
            return compendio_obj.pk
        create = False
    qs = instance.archivos.all()
    if create:
        compendio_obj = Compendio(
            nombre=filename,
            carpeta=instance,
        )

    compendio_obj.cantidad = len(qs)
    compendio_obj.hash = hash_data

    temp_file = get_zip_file(instance)
    compendio_obj.archivo = File(temp_file, filename)
    compendio_obj.save()
    temp_file.close()

    return compendio_obj.pk
