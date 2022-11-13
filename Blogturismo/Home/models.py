from django.db import models

# Create your models here.
class Destino (models.Model):
    
    lugar = models.CharField(max_length=40)
    dias = models.IntegerField()
    pension = models.CharField(max_length=40)

