from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.principal.urls')),
    path('', include('applications.personas.urls')),
    path('', include('applications.empleados.urls')),
]