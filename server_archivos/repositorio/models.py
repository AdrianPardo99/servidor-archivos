from django.db import models
from django.utils import timezone

from simple_history.models import HistoricalRecords

from core.models import BaseModel


class Software(BaseModel):
    nombre = models.TextField()
    documento = models.FileField(upload_to="software/")
    history = HistoricalRecords()

    class Meta:
        db_table = "software"
        verbose_name = "Software"
        verbose_name_plural = "Software"

    def __str__(self):
        return f"{self.pk} .- {self.nombre} * {self.documento} *"


class Carpeta(BaseModel):
    nombre = models.TextField()
    archivos = models.ManyToManyField(
        Software,
    )
    history = HistoricalRecords()

    class Meta:
        db_table = "carpeta"
        verbose_name = "Carpeta"
        verbose_name_plural = "Carpetas"

    def __str__(self):
        return f"{self.pk} .- {self.nombre}"


class Compendio(BaseModel):
    nombre = models.TextField()
    archivo = models.FileField(upload_to="zip/")
    cantidad = models.IntegerField()
    carpeta = models.OneToOneField(
        Carpeta,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        db_table = "compendio"
        verbose_name = "Compendio"
        verbose_name_plural = "Compendios"

    def __str__(self):
        return f"{self.pk} - {self.nombre} - {self.cantidad}"
