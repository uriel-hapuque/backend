# Generated by Django 5.1.2 on 2024-10-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduinos', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arduino',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='arduino',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]