# Generated by Django 5.1.7 on 2025-03-10 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0002_rename_type_reservation_v_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="vehicle",
            new_name="plate_number",
        ),
    ]
