from django import forms

class CrearDestinoForm(forms.Form):

    destino= forms.CharField(max_length=40)
    dias = forms.IntegerField()
    pension = forms.CharField(max_length=40)