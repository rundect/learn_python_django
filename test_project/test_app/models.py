from django.db import models


class WeatherApi(models.Model):
    url = models.URLField()
    password = models.CharField(max_length=100)
