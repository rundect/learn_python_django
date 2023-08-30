from django.urls import include, path
from .api.users.urls import user_urls
from .api.weather.urls import weather_api_urls


urlpatterns = [
    path('', include(user_urls)),
    path('', include(weather_api_urls))
]
