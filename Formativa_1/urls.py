"""Formativa_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/alumnos/')),
    # PANEL DE ADMINISTRACIÓN
    # Crea la URL /admin/ para acceder al panel de administración de Django
    # Ejemplo: localhost:8000/admin/
    path('admin/', admin.site.urls),
        # URLS DE LA APP ALUMNOS
    # Incluye todas las URLs definidas en alumnos/urls.py
    # Todas las URLs de la app empezarán con /alumnos/
    # Ejemplo: /alumnos/galeria/, /alumnos/contacto/, etc.
    path('alumnos/',include('alumnos.urls')),
      # SISTEMA DE AUTENTICACIÓN AUTOMÁTICO
    # Incluye todas las URLs de autenticación built-in de Django
    # Crea automáticamente: /accounts/login/, /accounts/logout/, 
    # /accounts/password_reset/, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
