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
"""
def destinos(request):
        lugares = Destino.objects.all()
        
    
        return render( request, 'destinos.html', {'lugares':lugares})
"""

"""destino1= Destino(d_lugar = 'BSAS', d_dias = 4, d_pension = 'Completa')
    destino2= Destino(d_lugar = 'Misiones', d_dias = 1, d_pension = 'Media')
    destino3= Destino(d_lugar = 'Corrientes', d_dias = 3, d_pension = 'No')*/
    return render( request, 'saludo.html', {'objetos':[destino1,destino2,destino3]} )"""

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
        lugar = request.GET['buscardestino']
        lugares = Destino.objects.filter(d_lugar__icontains= lugar)
    
        return render( request, 'destinos.html', {'lugares':lugares})
    
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




def crearexperiencia(request):
    return render(  request, 'crearexperiencia.html')

def experiencia(request):
    return render(  request, 'experiencia.html')

def nosotros(request):
    return render(  request, 'nosotros.html')



def solicituddestino(request):
    if request.method == 'POST':

        soldestinoform = SolDestinoForm(request.POST)

        if soldestinoform.is_valid():

            form_limpio = soldestinoform.cleaned_data
        
            soldestino = SolicitudDestino(
                        sd_nombre =form_limpio['nombre'],
                        sd_apellido =form_limpio['apellido'],
                        sd_numero =form_limpio['numero'],
                        sd_mail =form_limpio['mail'],
                        sd_lugar =form_limpio['lugar'],
                        sd_salida =form_limpio['salida'],)
            soldestino.save()

            return render(request, 'postingreso.html')

    else:
        soldestinoform =   SolDestinoForm()

    return render(  request, 'destinoform.html',{'soldestinoform':soldestinoform})


def solicitudhotel(request):
    if request.method == 'POST':

        solhotelform = SolHotelForm(request.POST)

        if solhotelform.is_valid():

            form_limpio = solhotelform.cleaned_data
        
            solhotel = SolicitudHotel(
                        sh_nombre =form_limpio['nombre'],
                        sh_apellido =form_limpio['apellido'],
                        sh_numero =form_limpio['numero'],
                        sh_mail =form_limpio['mail'],
                        sh_lugar =form_limpio['lugar'],
                        sh_hotel =form_limpio['hotel'],
                        sh_ingreso =form_limpio['ingreso'],)
            solhotel.save()

            return render(request, 'postingreso.html')

    else:
        solhotelform =   SolHotelForm()

    return render(  request, 'hotelform.html',{'solhotelform':solhotelform})


def buscarhotel(request):
    
    if request.GET.get ('buscarhotel',  False):
        lugar = request.GET['buscarhotel']
        lugares = Hotel.objects.filter(h_destino__icontains= lugar)
    
        return render( request, 'hotel.html', {'lugares':lugares})
    
    else:
        respuesta = 'No hay datos'  

        return render(request, 'buscarhotel.html',{'respuesta':respuesta})


def buscarexcursion(request):
    
    if request.GET.get ('buscarexcursion',  False):
        lugar = request.GET['buscarexcursion']
        lugares = Excursiones.objects.filter(e_lugar__icontains= lugar)
    
        return render( request, 'excursion.html', {'lugares':lugares})
    
    else:
        respuesta = 'No hay datos'  

        return render(request, 'buscarexcursion.html',{'respuesta':respuesta})


def solicitudexcursion(request):
    if request.method == 'POST':

        solexcursionform = SolExcursionForm(request.POST)

        if solexcursionform.is_valid():

            form_limpio = solexcursionform.cleaned_data
        
            solexcursion = SolicitudExcursion(
                        se_nombre =form_limpio['nombre'],
                        se_apellido =form_limpio['apellido'],
                        se_numero =form_limpio['numero'],
                        se_mail =form_limpio['mail'],
                        se_lugar =form_limpio['lugar'],
                        se_actividad =form_limpio['actividad'],
                        se_salida =form_limpio['salida'],)
            solexcursion.save()

            return render(request, 'postingreso.html')

    else:
        solexcursionform =   SolExcursionForm()

    return render(  request, 'excursionform.html',{'solexcursionform':solexcursionform})




def solicitudcontacto(request):
    if request.method == 'POST':

        solcontactoform = SolContactoForm(request.POST)

        if solcontactoform.is_valid():

            form_limpio = solcontactoform.cleaned_data
        
            solcontacto = SolicitudContacto(
                        c_nombre =form_limpio['nombre'],
                        c_apellido =form_limpio['apellido'],
                        c_numero =form_limpio['numero'],
                        c_mail =form_limpio['mail'],
                        c_pais =form_limpio['pais'],
                        c_provincia =form_limpio['provincia'],
                        c_ciudad =form_limpio['ciudad'],
                        c_consulta =form_limpio['consulta'],)
            solcontacto.save()

            return render(request, 'postingreso.html')

    else:
        solcontactoform =   SolContactoForm()

    return render(  request, 'contactoform.html',{'solcontactoform':solcontactoform})



