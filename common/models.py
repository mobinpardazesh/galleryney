from django.db import models

# Create your models here.
class Countries (models.Model):
    country_name=models.CharField(max_length=200)
    country_create_date=models.DateTimeField()
