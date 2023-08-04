# Generated by Django 4.0 on 2023-08-04 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=100)),
                ('storecompanyname', models.CharField(max_length=100)),
                ('storeURL', models.URLField()),
                ('sslenabled', models.BooleanField(default=False)),
                ('hostvalues', models.CharField(max_length=200)),
                ('displayorder', models.IntegerField(max_length=5)),
                ('storeaddress', models.CharField(max_length=200)),
                ('storephonenumber', models.CharField(max_length=100)),
                ('storevat', models.IntegerField(max_length=2)),
                ('defaultlanguage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.language')),
                ('storecityname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.citymodel')),
                ('storecountryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.countrymodel')),
                ('storeproviencename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.proviencemodel')),
            ],
        ),
    ]
