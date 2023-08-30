from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('test/', include('test_app.urls')),
    path('admin/', admin.site.urls),
]