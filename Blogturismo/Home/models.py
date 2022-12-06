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
    d_costo = models.DecimalField(max_digits=10,decimal_places=3)

# Clase de hoteles disponibles para alojarse
class Hotel (models.Model):
    h_destino = models.CharField(max_length=40)
    h_lugar = models.CharField(max_length=40)
    h_dias = models.IntegerField()
    h_pension = models.CharField(max_length=40)
    h_habitacion = models.CharField(max_length=40)
    h_ingreso = models.DateField()
    h_salida = models.DateField()
    h_costo = models.DecimalField(max_digits=10,decimal_places=3)

# Clase de excursiones disponibles para realizar
class Excursiones (models.Model):
    
    e_lugar = models.CharField(max_length=40)
    e_dias = models.IntegerField()
    e_actividad = models.CharField(max_length=40)
    e_dificultad = models.CharField(max_length=40)
    e_salida = models.DateField()
    e_regreso = models.DateField()
    e_costo = models.DecimalField(max_digits=10,decimal_places=3)


class CrearDestino (models.Model):
    
    cd_nombre = models.CharField(max_length=40)
    cd_apellido = models.CharField(max_length=40)
    cd_numero = models.IntegerField()
    cd_mail = models.CharField(max_length=100)
    cd_lugar = models.CharField(max_length=40)
    cd_salida = models.DateField()


class CrearExcursion (models.Model):
    
    ce_lugar = models.CharField(max_length=40)
    ce_dias = models.IntegerField()
    ce_actividad = models.CharField(max_length=40)
    ce_dificultad = models.CharField(max_length=40)
    ce_salida = models.DateField()
    ce_regreso= models.DateField()

class CrearHotel (models.Model):
    
    ch_lugar = models.CharField(max_length=40)
    ch_dias = models.IntegerField()
    ch_pension = models.CharField(max_length=40)
    ch_habitacion = models.CharField(max_length=40)
    ch_salida = models.DateField()
    ch_regreso= models.DateField()



class SolicitudDestino (models.Model):
    
    sd_nombre = models.CharField(max_length=40)
    sd_apellido = models.CharField(max_length=40)
    sd_numero = models.IntegerField()
    sd_mail = models.CharField(max_length=100)
    sd_lugar = models.CharField(max_length=40)
    sd_salida = models.DateField()


class SolicitudHotel (models.Model):
    
    sh_nombre = models.CharField(max_length=40)
    sh_apellido = models.CharField(max_length=40)
    sh_numero = models.IntegerField()
    sh_mail = models.CharField(max_length=100)
    sh_lugar = models.CharField(max_length=40)
    sh_hotel = models.CharField(max_length=40)
    sh_ingreso = models.DateField()

class SolicitudExcursion (models.Model):
    
    se_nombre = models.CharField(max_length=40)
    se_apellido = models.CharField(max_length=40)
    se_numero = models.IntegerField()
    se_mail = models.CharField(max_length=100)
    se_lugar = models.CharField(max_length=40)
    se_actividad = models.CharField(max_length=40)
    se_salida = models.DateField()


class SolicitudContacto (models.Model):
    
    c_nombre = models.CharField(max_length=40)
    c_apellido = models.CharField(max_length=40)
    c_numero = models.IntegerField()
    c_mail = models.CharField(max_length=100)
    c_pais = models.CharField(max_length=40)
    c_provincia = models.CharField(max_length=40)
    c_ciudad = models.CharField(max_length=40)
    c_consulta = models.CharField(max_length=100)


