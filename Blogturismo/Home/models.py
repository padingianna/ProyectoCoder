from django.db import models
import datetime
#AGREGAR PRECIO A LOS MODELOS
# Clase de destino disponibles para viajar
class Destino (models.Model):
    
    d_lugar = models.CharField(max_length=40)
    d_dias = models.IntegerField()
    d_pension = models.CharField(max_length=40)
    d_salida = models.DateField()
    d_regreso= models.DateField()
    d_costo = models.BooleanField(max_length=20)

# Clase de hoteles disponibles para alojarse
class Hotel (models.Model):
    
    h_lugar = models.CharField(max_length=40)
    h_dias = models.IntegerField()
    h_pension = models.CharField(max_length=40)
    h_habitacion = models.CharField(max_length=40)
    h_salida = models.DateField()
    h_regreso= models.DateField()
    h_costo = models.BooleanField(max_length=20)

# Clase de excursiones disponibles para realizar
class Excursiones (models.Model):
    
    e_lugar = models.CharField(max_length=40)
    e_dias = models.IntegerField()
    e_actividad = models.CharField(max_length=40)
    e_dificultad = models.CharField(max_length=40)
    e_salida = models.DateField()
    e_regreso= models.DateField()
    e_costo = models.BooleanField(max_length=20)


class CrearDestino (models.Model):
    
    cd_lugar = models.CharField(max_length=40)
    cd_dias = models.IntegerField()
    cd_pension = models.CharField(max_length=40)
    cd_salida = models.DateField()
    cd_regreso= models.DateField()