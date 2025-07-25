# Generated by Django 5.2.1 on 2025-06-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='espacios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField(verbose_name='disponible')),
                ('reservado', models.TextField(verbose_name='reservado')),
                ('discapacitado', models.IntegerField(verbose_name='discapacitados')),
                ('electrico', models.IntegerField(verbose_name='electrico')),
                ('moto', models.IntegerField(verbose_name='moto')),
                ('tarifa_id', models.IntegerField(verbose_name='tarifa')),
            ],
        ),
    ]
