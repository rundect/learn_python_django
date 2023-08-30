from rest_framework import serializers
from ...models import WeatherApi


class WeatherAPISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherApi
        fields = ['url', 'password']

