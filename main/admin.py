from django.contrib import admin

from .models import CurrencyRate


@admin.register(CurrencyRate)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['currency', 'rate']
