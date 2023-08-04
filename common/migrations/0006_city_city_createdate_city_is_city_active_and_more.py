# Generated by Django 4.0 on 2023-08-03 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_rename_iso_code_long_country_country_iso_code_long_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_createdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='city',
            name='is_city_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='city',
            name='is_provience_center',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='country',
            name='country_center',
            field=models.CharField(max_length=200, null=True, verbose_name='Country Center'),
        ),
        migrations.AddField(
            model_name='country',
            name='is_country_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provience',
            name='is_country_center',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='provience',
            name='is_provience_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provience',
            name='provience_center',
            field=models.CharField(max_length=10, null=True, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='provience',
            name='provience_center_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Provience Code'),
        ),
        migrations.AddField(
            model_name='provience',
            name='provience_createdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]