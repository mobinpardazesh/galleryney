from django.contrib import admin
from .models import Countries, Proviences, Cities


class CountriesAdmin(admin.ModelAdmin):
    list_display = ("country_name")


admin.site.register(Countries)


class ProviencesAmin(admin.ModelAdmin):
    list_display = ("provience_name")


admin.site.register(Proviences)


class CitiesAdmin(admin.ModelAdmin):
    list_display = ("citoes_name")


admin.site.register(Cities)
