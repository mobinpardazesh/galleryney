from django.contrib import admin
# from common.models import Countrymodel, Proviencemodel, Citymodel
import common.models


@admin.register(common.models.Countrymodel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("is_country_active","country_name","country_code","country_center","country_iso_code_short","country_iso_code_long","country_createdate")


@admin.register(common.models.Proviencemodel)
class ProvienceAmin(admin.ModelAdmin):
    list_display = ("is_provience_active","provience_name","provience_center","provience_center_code","is_country_center","provience_createdate")


@admin.register(common.models.Citymodel)
class CityAdmin(admin.ModelAdmin):
    list_display = ("is_city_active","city_name","is_provience_center","city_createdate")
