from django.urls import include, path
from rest_framework import routers
from .api.users.urls import user_urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(user_urls))
]
