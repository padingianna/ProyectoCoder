from django.shortcuts import render
from django.http import HttpResponse
from .models import Destino
from .forms import CrearDestinoForm

def saludo(request):
    return HttpResponse('respeta o proceso')
# Create your views here.
def index1(request):
    return render(  request, 'index.html')


"""
def versaludo(request):
    destino= Destino(lugar = 'BSAS', dias = 4, pension = 'Completa')
    return render( request, 'saludo.html', { 'lugar': destino.lugar, 'dias': destino.dias, 'pension': destino.pension})
"""

def versaludo(request):
    destino1= Destino(lugar = 'BSAS', dias = 4, pension = 'Completa')
    destino2= Destino(lugar = 'Misiones', dias = 1, pension = 'Media')
    destino3= Destino(lugar = 'Corrientes', dias = 3, pension = 'No')
    return render( request, 'saludo.html', {'objetos':[destino1,destino2,destino3]} )


def prueba(request):
    return render(  request, 'index1.html')

""" Forma 1 de formulario
def ingreso(request):
    if request.method == 'POST':
        
        destino = Destino(lugar=request.POST['destino'],dias=request.POST['dias'],pension=request.POST['pension'])
        
        destino.save()

        return render(request, 'index.html')

    return render(  request, 'formulario.html')
"""

def ingreso(request):
    if request.method == 'POST':

        formulario = CrearDestinoForm(request.POST)

        if formulario.is_valid():

            form_limpio = formulario.cleaned_data
        
            destino = Destino(lugar=form_limpio['destino'],dias=form_limpio['dias'],pension=form_limpio['pension'])
            
            destino.save()

            return render(request, 'index.html')

    else:
        formulario = CrearDestinoForm()

    return render(  request, 'formulario.html',{'formulario':formulario})


def buscar(request):


    
    return render(  request, 'buscar.html')