from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse('respeta o proceso')
# Create your views here.

def versaludo(request):
    return render(  request, 'saludo.html')

def index1(request):
    return render( request, 'index.html')