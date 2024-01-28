from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Carpeta
from .tasks import create_and_save_zip


@receiver(post_save, sender=Carpeta)
def genera_zip(sender, instance, created, **kwargs):
    create_and_save_zip.delay(instance.pk)
