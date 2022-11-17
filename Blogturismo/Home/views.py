from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CrearDestinoForm
from datetime import datetime




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

def ingreso(request):
    if request.method == 'POST':

        formulario = CrearDestinoForm(request.POST)

        if formulario.is_valid():

            form_limpio = formulario.cleaned_data
        
            destino = CrearDestino(cd_lugar=form_limpio['lugar'],
                        cd_dias=form_limpio['dias'],
                        cd_pension=form_limpio['pension'], 
                        cd_salida=form_limpio['salida'],
                        cd_regreso=form_limpio['regreso'])
            

            
            destino.save()

            return render(request, 'index.html')

    else:
        formulario = CrearDestinoForm()

    return render(  request, 'formulario.html',{'formulario':formulario})


def buscar(request):
    
    if request.GET.get ('buscardestino',  False):
        lugar1 = request.GET['buscardestino']
        lugares = Destino.objects.filter(d_lugar__icontains= lugar1)
    
        return render( request, 'buscar.html', {'lugares':lugares})
    
    else:
        respuesta = 'No hay datos'

        return render(request, 'buscar.html',{'respuesta':respuesta})
