# Generated by Django 5.1.2 on 2024-10-24 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_detections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water_Data',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('water_level', models.FloatField()),
                ('dissolved_solids', models.FloatField()),
                ('data_detection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data_detections.data_detection')),
            ],
        ),
    ]
