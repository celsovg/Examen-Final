from django import forms
from apps.tienda.models import Tienda

class RegistroTiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda

        fields =[
        'nombre',
        'nombre_sucursal',
        'direccion',
        'ciudad',
        'region',
        ]
        labels = {
        'nombre':'Nombre',
        'nombre_sucursal':'Nombre sucursal',
        'direccion':'Direccion',
        'ciudad':'Ciudad',
        'region':'Region',
        }
        widgets = {
        'nombre':forms.TextInput(attrs={'class': 'form-control'}),
        'nombre_sucursal':forms.TextInput(attrs={'class': 'form-control'}),
        'direccion':forms.TextInput(attrs={'class': 'form-control'}),
        'ciudad':forms.TextInput(attrs={'class': 'form-control'}),
        'region':forms.TextInput(attrs={'class': 'form-control'}),

        }