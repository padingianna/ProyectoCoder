from django import forms

class CrearDestinoForm(forms.Form):

    lugar = forms.CharField(max_length=40)
    dias = forms.IntegerField()
    pension = forms.CharField(max_length=40)
    salida = forms.DateField()
    regreso= forms.DateField()