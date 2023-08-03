from django.db import models
from django.utils import timezone
# Create your models here.

class Country(models.Model):
    is_country_active=models.BooleanField(default=True)
    country_name = models.CharField('Country',max_length=200,default="iran" ,null=True, blank=True)
    country_code = models.CharField('Code', max_length=10, null=True)
    country_center=models.CharField('Country Center',max_length="200")
    is_country_active=models.BooleanField(default=True)
    country_iso_code_short = models.CharField('ISO Code Short', max_length=2, null=True)
    country_iso_code_long = models.CharField('ISO Code Long', max_length=3, null=True)
    country_createdate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.country_name

class Provience(models.Model):
    is_provience_active=models.BooleanField(default=True)
    provience_name = models.CharField('Provience',max_length=200,null=True)
    provience_center = models.CharField('Code', max_length=10, null=True)
    provience_center_code = models.CharField('Provience Code', max_length=10, null=True)
    is_country_center=models.BooleanField(default=False)
    provience_createdate=models.DateTimeField(default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.provience_name

class City(models.Model):
    is_city_active=models.BooleanField(default=True)
    city_name = models.CharField('City',max_length=200,null=True)
    is_provience_center=models.BooleanField(default=False)
    city_createdate=models.DateTimeField(default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    provience = models.ForeignKey(Provience, on_delete=models.CASCADE)


    def __str__(self):
        return self.city_name
