# Generated by Django 5.1.7 on 2025-03-10 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vehicles", "0002_rename_group_vehicle_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("type", models.CharField(max_length=10)),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.vehicle",
                    ),
                ),
            ],
        ),
    ]
