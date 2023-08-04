from django.contrib import admin
from .models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("languagename",)

# Register your models here.
