# Generated by Django 4.0 on 2023-08-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_city_city_name_alter_country_country_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='country',
            name='iso_code_long',
            field=models.CharField(max_length=3, null=True, verbose_name='ISO Code Long'),
        ),
        migrations.AddField(
            model_name='country',
            name='iso_code_short',
            field=models.CharField(max_length=2, null=True, verbose_name='ISO Code Short'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(blank=True, default='iran', max_length=200, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='provience',
            name='provience_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Provience'),
        ),
    ]
