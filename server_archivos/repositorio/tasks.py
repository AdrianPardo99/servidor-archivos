from django.core.files import File

from celery import shared_task

from .models import Carpeta, Compendio
from .utils import get_zip_file


@shared_task
def create_and_save_zip(carpeta_id):
    instance = Carpeta.objects.get(pk=carpeta_id)
    compendio_obj = Compendio.objects.filter(carpeta=instance)
    filename = f"{instance.nombre}_output.zip"

    if compendio_obj:
        compendio_obj = compendio_obj.first()
        if compendio_obj.cantidad == len(instance.archivos.all()):
            return compendio_obj.pk
        compendio_obj.cantidad = len(instance.archivos.all())
    else:
        compendio_obj = Compendio(
            nombre=filename,
            cantidad=len(instance.archivos.all()),
            carpeta=instance,
        )
    temp_file = get_zip_file(instance)
    compendio_obj.archivo = File(temp_file, filename)
    compendio_obj.save()
    temp_file.close()
    return compendio_obj.pk
