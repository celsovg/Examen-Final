from django import forms
from .models import RegistroUsuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(forms.ModelForm):

    class Meta:
        model = RegistroUsuario

        fields = [
            'nombre',
            'apellido',
            'correo',
            'contraseña',
            'fecha_nacimiento',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo electronico',
            'contraseña': 'Contraseña',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widget = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'contraseña': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.MultipleChoiceField(),
        }


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electronico',
        }
