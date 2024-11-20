from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('', include('AsistenciaApp.urls')),  # Incluye las URLs de la aplicación principal
    path('accounts/', include('django.contrib.auth.urls')),  # URLs para login/logout y autenticación
]
