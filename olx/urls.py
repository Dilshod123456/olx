"""
URL configuration for olx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import kirish, malumotlar, elektronika, telefon, Iphone, Iphone15pro, Titanium, harid, Planshet, AirPods


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kirish),
    path('malumotlar/', malumotlar),
    path('malumotlar/elektronika/', elektronika),
    path('malumotlar/elektronika/telefon/', telefon),
    path('malumotlar/elektronika/telefon/Iphone/', Iphone),
    path('malumotlar/elektronika/telefon/Iphone/Iphone15pro/', Iphone15pro),
    path('malumotlar/elektronika/telefon/Iphone/Iphone15pro/Titanium/', Titanium),
    path('malumotlar/elektronika/telefon/Iphone/Iphone15pro/Titanium/harid', harid),
    path('malumotlar/elektronika/planshet/', Planshet),
    path('malumotlar/elektronika/AirPods', AirPods),


]
