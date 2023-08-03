from django.contrib import admin
from .models import Country, Provience, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name",)


@admin.register(Provience)
class ProvienceAmin(admin.ModelAdmin):
    list_display = ("provience_name","id")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("city_name",)
