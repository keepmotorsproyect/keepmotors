# Generated by Django 5.2.3 on 2025-06-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0003_alter_entrada_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='mes',
            field=models.CharField(max_length=20, verbose_name='mes'),
        ),
    ]
