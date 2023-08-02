from django.db import models

# Create your models here.
class Countries (models.Model):
    country_name=models.CharField(max_length=200)
    country_create_date=models.DateTimeField()

class Proviences (models.Model):
    provience_name=models.CharField(max_length=200)
    provience_create_date=models.DateTimeField()

class Cities (models.Model):
    city_name=models.CharField(max_length=200)
    city_create_date=models.DateTimeField()