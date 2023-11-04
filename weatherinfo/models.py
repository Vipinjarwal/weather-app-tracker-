from django.db import models


class HistoricalData(models.Model):
    city_id = models.PositiveIntegerField()
    city_name = models.CharField(max_length=255)
    findname = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    lon = models.FloatField()
    lat = models.FloatField()
    time = models.DateTimeField()

    temp = models.FloatField()
    pressure = models.PositiveIntegerField()
    humidity = models.PositiveIntegerField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()

    wind_speed = models.FloatField()
    clouds_all = models.PositiveIntegerField()
    weather_id = models.PositiveIntegerField()
    weather_main = models.CharField(max_length=255)
    weather_description = models.CharField(max_length=255)
    weather_icon = models.CharField(max_length=10)

    def __str__(self):
        return self.city_name  # Use a relevant field for the string representation
