from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Destino)
admin.site.register(Excursiones)
admin.site.register(Hotel)
admin.site.register(SolicitudDestino)
admin.site.register(SolicitudExcursion)
admin.site.register(SolicitudHotel)
admin.site.register(CrearDestino)
admin.site.register(CrearExcursion)
admin.site.register(CrearHotel)