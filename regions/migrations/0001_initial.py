# Generated by Django 5.1.2 on 2024-10-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=255)),
            ],
        ),
    ]
