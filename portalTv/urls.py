"""portalTv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.Registro.urls')),
    path('', include('apps.Usuario.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name= 'login'),
    #login y logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='Usuario/login.html'),
    name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
]
