# Generated by Django 4.0 on 2023-08-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_proviences_countries_alter_countries_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='country_date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='country_name',
            field=models.CharField(max_length=200),
        ),
    ]