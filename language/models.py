from django.db import models

# Create your models here.

class Language (models.Model):
    languagename=models.CharField(max_length=100)

    def __str__(self):
        self.languagename
