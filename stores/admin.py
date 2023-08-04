from django.contrib import admin
from .models import Storemodel


@admin.register(Storemodel)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("storename","storecompanyname","storeURL","sslenabled","hostvalues","defaultlanguage","displayorder","storecountryname","storeproviencename","storecityname","storeaddress","storephonenumber","storevat")

