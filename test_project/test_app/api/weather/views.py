from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WeatherAPISerializer
from ...models import WeatherApi


class WeatherAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WeatherApi.objects.all().order_by('id')
    serializer_class = WeatherAPISerializer
    permission_classes = [permissions.IsAuthenticated]

