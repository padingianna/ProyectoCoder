"""Blogturismo URL Configuration

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
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index1,name='Home'),
    path( 'saludo/', views.saludo,name='saludo'),
    path( 'destinos/', views.buscar,name='Destinos'),
    path('prueba', views.prueba,name='prueba'),
    path('Crear tu Destino', views.creardestino,name='Crear tu Destino'),
    path('Crear tu Excursion', views.crearexcursion,name='Crear tu Excursion'),
    path('Crear tu Hotel', views.crearhotel,name='Crear tu Hotel'),
    path('Buscar', views.buscar,name='buscar'),

]