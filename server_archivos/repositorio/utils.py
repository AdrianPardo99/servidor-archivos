import os
import tempfile
import zipfile

from .models import Carpeta


def get_extension(filename):
    base_name = os.path.basename(filename)
    parts = base_name.split(".")
    if bool(parts):
        extension = "." + ".".join(parts[1:])
    else:
        extension = ""
    return extension


def get_zip_file(instance: Carpeta):
    temp_file = tempfile.TemporaryFile()

    with zipfile.ZipFile(temp_file, "w", zipfile.ZIP_DEFLATED) as zip_stream:
        for archivo in instance.archivos.all():
            extension = get_extension(archivo.documento.name)
            file_name = archivo.nombre + extension
            zip_stream.write(archivo.documento.path, arcname=file_name)
    temp_file.seek(0)
    return temp_file
