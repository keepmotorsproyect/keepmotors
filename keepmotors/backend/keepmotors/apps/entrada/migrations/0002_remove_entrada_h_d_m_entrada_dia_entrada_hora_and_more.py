# Generated by Django 5.2.3 on 2025-06-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='h_d_m',
        ),
        migrations.AddField(
            model_name='entrada',
            name='dia',
            field=models.IntegerField(default=1, verbose_name='dia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='hora',
            field=models.IntegerField(default=1, verbose_name='hora'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='mes',
            field=models.IntegerField(default=1, verbose_name='mes'),
            preserve_default=False,
        ),
    ]
