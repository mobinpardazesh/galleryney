from django.contrib import admin
from .models import Countries, Proviences, Cities


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ("country_name",)


@admin.register(Proviences)
class ProviencesAmin(admin.ModelAdmin):
    list_display = ("provience_name",)


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ("citoes_name",)
