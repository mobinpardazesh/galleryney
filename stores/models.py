from django.db import models
# from django.utils import timezone

from common.models import Countrymodel, Proviencemodel, Citymodel
from language.models import Language


# Create your models here.

class Storemodel (models.Model):
    storename=models.CharField(max_length=100)
    storecompanyname=models.CharField(max_length=100)
    storeURL=models.URLField(max_length=200)
    sslenabled=models.BooleanField(default=False)
    hostvalues=models.CharField(max_length=200)
    defaultlanguage=models.ForeignKey(Language,on_delete=models.CASCADE)
    displayorder=models.IntegerField()
    storecountryname=models.ForeignKey(Countrymodel,on_delete=models.CASCADE)
    storeproviencename=models.ForeignKey(Proviencemodel,on_delete=models.CASCADE)
    storecityname=models.ForeignKey(Citymodel,on_delete=models.CASCADE)
    storeaddress=models.CharField(max_length=200)
    storephonenumber=models.CharField(max_length=100)
    storevat=models.IntegerField()

    def __str__(self):
        return self.storename


