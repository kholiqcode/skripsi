"""skripsi URL Configuration

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
from django.urls import path

from sentiment.views import cyberbullying, dashboard, emotion, general, profils, sentiment, user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general),
    path('user', user),
    path('cyberbullying', cyberbullying),
    path('emotion', emotion),
    path('dashboard', dashboard),
    path('profils', profils),
    path('sentiment', sentiment),
]
