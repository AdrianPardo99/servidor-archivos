from django.db import models
from django.db.models.query import QuerySet


class SoftQuerySet(QuerySet):
    def delete(self):
        # Actualiza el estado de eliminacion logica
        return super(SoftQuerySet, self).update(activo=False)

    def hard_delete(self):
        # Elimina totalmente el objeto
        return super(SoftQuerySet, self).delete()

    def alive(self):
        # Filtra aquellos objetos activos
        return self.filter(activo=True)

    def dead(self):
        # Filtra aquellos objetos eliminados logicamente
        return self.exclude(activo=True)


class SoftDeleteManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop("alive_only", True)
        super(SoftDeleteManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        # Obtiene los objetos de cada modelo de acuerdo a su configuracion
        if self.alive_only:
            return SoftQuerySet(self.model).filter(activo=self.alive_only)
        # Obtiene todos los objetos incluidos los eliminados logicamente
        return SoftQuerySet(self.model)

    def hard_delete(self):
        # Eliminacion directa de todos los objetos del modelo
        return self.get_queryset().hard_delete()


class BaseModelSoftDelete(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager(alive_only=False)

    def delete(self):
        # Permite hacer un delete logico en la BD
        self.activo = False
        self.save()

    def recover(self):
        # Permite recuperar un objeto
        self.activo = True
        self.save()

    def hard_delete(self):
        # Hace una eliminacion directa
        super().delete()

    class Meta:
        abstract = True


class BaseModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
