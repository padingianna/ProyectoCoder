from django import forms
from .models import SolicitudContacto

from django.contrib.auth.models import * 
from django.contrib.auth.forms import *

class SolDestinoForm(forms.Form):

    lugar = forms.CharField(max_length=40)
    dias = forms.IntegerField()
    pension = forms.CharField(max_length=40)
    salida = forms.DateField()
    regreso = forms.DateField()

class CrearExcursionForm(forms.Form):

    lugar = forms.CharField(max_length=40)
    dias = forms.IntegerField()
    actividad = forms.CharField(max_length=40)
    dificultad = forms.CharField(max_length=40)
    salida = forms.DateField()
    regreso = forms.DateField()

class CrearHotelForm (forms.Form):
    
    lugar = forms.CharField(max_length=40)
    dias = forms.IntegerField()
    pension = forms.CharField(max_length=40)
    habitacion = forms.CharField(max_length=40)
    salida = forms.DateField()
    regreso= forms.DateField()


class SolDestinoForm(forms.Form):

    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    mail = forms.CharField(max_length=100)
    lugar = forms.CharField(max_length=40)
    salida = forms.DateField()


class SolHotelForm(forms.Form):

    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    mail = forms.CharField(max_length=100)
    lugar = forms.CharField(max_length=40)
    hotel = forms.CharField(max_length=40)
    ingreso = forms.DateField()

class SolExcursionForm(forms.Form):

    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    mail = forms.CharField(max_length=100)
    lugar = forms.CharField(max_length=40)
    actividad = forms.CharField(max_length=40)
    salida = forms.DateField()

class SolContactoForm (forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    mail = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=40)
    consulta = forms.CharField(max_length=100, widget=forms.Textarea(),)





