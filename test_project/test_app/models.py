from django.db import models


class WeatherApi(models.Model):
    url = models.URLField()
    password = models.CharField(max_length=100)


class WeatherLocation(models.Model):
    name = models.CharField(max_length=50),
    region = models.CharField(max_length=50),
    country = models.CharField(max_length=50),
    lat = models.DecimalField(max_digits=5, decimal_places=2),
    lon = models.DecimalField(max_digits=5, decimal_places=2),
    tz_id = models.CharField(max_length=50),
    localtime_epoch = models.IntegerField(),
    localtime = models.DateTimeField(),


class WeatherInfo(models.Model):
    last_updated_epoch = models.IntegerField(),
    last_updated = models.DateTimeField(),
    temp_c = models.DecimalField(max_digits=5, decimal_places=2),
    temp_f = models.DecimalField(max_digits=5, decimal_places=2),
    is_day = models.IntegerField(),
    condition = models.JSONField(),
    wind_mph = models.DecimalField(max_digits=5, decimal_places=2),
    wind_kph = models.DecimalField(max_digits=5, decimal_places=2),
    wind_degree = models.IntegerField(),
    wind_dir = models.CharField(max_length=10),
    pressure_mb = models.DecimalField(max_digits=5, decimal_places=2),
    pressure_in = models.DecimalField(max_digits=5, decimal_places=2),
    precip_mm = models.DecimalField(max_digits=5, decimal_places=2),
    precip_in = models.DecimalField(max_digits=5, decimal_places=2),
    humidity = models.IntegerField(),
    cloud = models.IntegerField(),
    feelslike_c = models.DecimalField(max_digits=5, decimal_places=2),
    feelslike_f = models.DecimalField(max_digits=5, decimal_places=2),
    vis_km = models.DecimalField(max_digits=5, decimal_places=2),
    vis_miles = models.DecimalField(max_digits=5, decimal_places=2),
    uv = models.DecimalField(max_digits=5, decimal_places=2),
    gust_mph = models.DecimalField(max_digits=5, decimal_places=2),
    gust_kph = models.DecimalField(max_digits=5, decimal_places=2)
