from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import *

def saludo(request):
    return HttpResponse('respeta o proceso')
# Create your views here.
def index1(request):
    return render(  request, 'index.html')

"""
def versaludo(request):
    destino= Destino(d_lugar = 'BSAS', d_dias = 4, d_pension = 'Completa')
    return render( request, 'saludo.html', { 'lugar': destino.d_lugar, 'dias': destino.d_dias, 'pension': destino.d_pension})
"""

def versaludo(request):
    destino1= Destino(d_lugar = 'BSAS', d_dias = 4, d_pension = 'Completa')
    destino2= Destino(d_lugar = 'Misiones', d_dias = 1, d_pension = 'Media')
    destino3= Destino(d_lugar = 'Corrientes', d_dias = 3, d_pension = 'No')
    return render( request, 'saludo.html', {'objetos':[destino1,destino2,destino3]} )

def prueba(request):
    return render(  request, 'index1.html')

""" Forma 1 de formulario
def ingreso(request):
    if request.method == 'POST':
        
        destino = Destino(d_lugar=request.POST['destino'],d_dias=request.POST['dias'],d_pension=request.POST['pension'])
        
        destino.save()

        return render(request, 'index.html')

    return render(  request, 'formulario.html')
"""

def creardestino(request):
    if request.method == 'POST':

        destinoform = CrearDestinoForm(request.POST)

        if destinoform.is_valid():

            form_limpio = destinoform.cleaned_data
        
            destino = CrearDestino(cd_lugar=form_limpio['lugar'],
                        cd_dias=form_limpio['dias'],
                        cd_pension=form_limpio['pension'], 
                        cd_salida=form_limpio['salida'],
                        cd_regreso=form_limpio['regreso'])
            
            destino.save()

            return render(request, 'index.html')

    else:
        destinoform = CrearDestinoForm()

    return render(  request, 'destinoform.html',{'destinoform':destinoform})

def buscar(request):
    
    if request.GET.get ('buscardestino',  False):
        lugar1 = request.GET['buscardestino']
        lugares = Destino.objects.filter(d_lugar__icontains= lugar1)
    
        return render( request, 'buscar.html', {'lugares':lugares})
    
    else:
        respuesta = 'No hay datos'

        return render(request, 'buscar.html',{'respuesta':respuesta})

def crearexcursion(request):
    if request.method == 'POST':

        excursionform = CrearExcursionForm(request.POST)

        if excursionform.is_valid():

            form_limpio = excursionform.cleaned_data

            excursion = CrearExcursion(
                        ce_lugar = form_limpio['lugar'],
                        ce_dias = form_limpio['dias'],
                        ce_actividad = form_limpio['actividad'],
                        ce_dificultad = form_limpio['dificultad'],
                        ce_salida = form_limpio['salida'],
                        ce_regreso= form_limpio['regreso'])

            
            excursion.save()

            return render(request, 'index.html')

    else:
        excursionform = CrearExcursionForm()

    return render(  request, 'excursionform.html',{'excursionform':excursionform})


def crearhotel(request):
    if request.method == 'POST':

        hotelform = CrearHotelForm(request.POST)

        if hotelform.is_valid():

            form_limpio = hotelform.cleaned_data

            hotel = CrearHotel(
                    ch_lugar = form_limpio['lugar'],
                    ch_dias = form_limpio['dias'],
                    ch_pension = form_limpio['pension'],
                    ch_habitacion = form_limpio['habitacion'],
                    ch_salida = form_limpio['salida'],
                    ch_regreso= form_limpio['regreso'])
            
            hotel.save()

            return render(request, 'index.html')

    else:
        hotelform = CrearHotelForm()

    return render(  request, 'hotelform.html',{'hotelform':hotelform})
