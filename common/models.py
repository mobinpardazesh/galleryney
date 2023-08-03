from django.db import models
# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=200,default="iran")
    def __str__(self):
        return self.country_name

class Provience(models.Model):
    provience_name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.provience_name

class City(models.Model):
    city_name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    provience = models.ForeignKey(Provience, on_delete=models.CASCADE)


    def __str__(self):
        return self.city_name
