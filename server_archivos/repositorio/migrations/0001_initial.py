# Generated by Django 5.0.1 on 2024-01-28 16:57

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Software",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creacion", models.DateTimeField(auto_now_add=True)),
                ("actualizado", models.DateTimeField(auto_now=True)),
                ("activo", models.BooleanField(default=True)),
                ("nombre", models.TextField()),
                ("documento", models.FileField(upload_to="software/")),
            ],
            options={
                "verbose_name": "Software",
                "verbose_name_plural": "Software",
                "db_table": "software",
            },
        ),
        migrations.CreateModel(
            name="HistoricalCarpeta",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("creacion", models.DateTimeField(blank=True, editable=False)),
                ("actualizado", models.DateTimeField(blank=True, editable=False)),
                ("activo", models.BooleanField(default=True)),
                ("nombre", models.TextField()),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.TextField(null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Carpeta",
                "verbose_name_plural": "historical Carpetas",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalSoftware",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("creacion", models.DateTimeField(blank=True, editable=False)),
                ("actualizado", models.DateTimeField(blank=True, editable=False)),
                ("activo", models.BooleanField(default=True)),
                ("nombre", models.TextField()),
                ("documento", models.TextField(max_length=100)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.TextField(null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Software",
                "verbose_name_plural": "historical Software",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Carpeta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creacion", models.DateTimeField(auto_now_add=True)),
                ("actualizado", models.DateTimeField(auto_now=True)),
                ("activo", models.BooleanField(default=True)),
                ("nombre", models.TextField()),
                ("archivos", models.ManyToManyField(to="repositorio.software")),
            ],
            options={
                "verbose_name": "Carpeta",
                "verbose_name_plural": "Carpetas",
                "db_table": "carpeta",
            },
        ),
    ]
