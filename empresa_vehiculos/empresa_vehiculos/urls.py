from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_vehiculos/', include('gestion_vehiculos.urls')),
]
