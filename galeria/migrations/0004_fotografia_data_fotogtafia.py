# Generated by Django 4.2.6 on 2023-10-14 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0003_fotografia_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotogtafia",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]