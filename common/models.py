from django.db import models


# Create your models here.

class Countries(models.Model):
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return self.country_name


class Proviences(models.Model):
    provience_name = models.CharField(max_length=200)

    def __str__(self):
        return self.provience_name


class Cities(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name
