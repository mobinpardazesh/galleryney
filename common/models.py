from django.db import models
# Create your models here.

class Country(models.Model):
    country_name = models.CharField('Country',max_length=200,default="iran" ,null=True, blank=True)
    country_code = models.CharField('Code', max_length=10, null=True)
    country_iso_code_short = models.CharField('ISO Code Short', max_length=2, null=True)
    country_iso_code_long = models.CharField('ISO Code Long', max_length=3, null=True)
    country_createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name

class Provience(models.Model):
    provience_name = models.CharField('Provience',max_length=200,null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.provience_name

class City(models.Model):
    city_name = models.CharField('City',max_length=200,null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    provience = models.ForeignKey(Provience, on_delete=models.CASCADE)


    def __str__(self):
        return self.city_name
