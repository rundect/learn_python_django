from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'weather_api', views.WeatherAPIView)


weather_api_urls = [
    path('', include(router.urls))
]
