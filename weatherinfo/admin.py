from django.contrib import admin
from .models import HistoricalData

# Register your models here.


class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ("city_name", "country", "temp", "weather_description", "time")


admin.site.register(HistoricalData, HistoricalDataAdmin)
