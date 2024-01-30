import os

from django.core.files.storage import FileSystemStorage
from django.conf import settings


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # Si el archivo ya existe, elimínalo para que pueda ser reemplazado
        # Solo usar de ser necesario
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
