from django import forms
from .models import Producto, ListaDeCompras
from apps.tienda.models import Tienda


class ProductoForm(forms.ModelForm):

    class Meta:

        model = Producto

        fields = [
            'nombre',
            'costo_real',
            'costo_presupuestado',
            'tienda',
            'notas',
            'comprado',
        ]
        labels = {
            'nombre': 'Nombre',
            'costo_real': 'Costo real',
            'costo_presupuestado': 'Costo Presupuestado',
            'tienda': 'Tienda',
            'notas': 'Notas adicionales',
            'comprado': '¿Comprado?',
        }
        widget = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_real': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_presupuestado': forms.TextInput(attrs={'class': 'form-control'}),
            'tienda': forms.Select(attrs={'class': 'form-control'}),
            'notas': forms.TextInput(attrs={'class': 'form-control'}),
            'comprado': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ListaDeComprasForm(forms.ModelForm):
    class Meta:
        model = ListaDeCompras

        fields = [
            'nombre_lista',
            'creador',
            'productos',
            'cantidad_productos',
            'cantidad_comprados',
            'presupuesto_total',
            'total_final',
        ]
        labels = {
            'nombre_lista': 'Nombre lista',
            'creador': 'Usuario',
            'productos':'Productos:',
            'cantidad_productos':'Cantidad de productos',
            'cantidad_comprados': 'N° de productos comprados',
            'presupuesto_total':'Costo presupuestado total',
            'total_final':'Costo real total',
        }
        widget = {
            'nombre_lista': forms.TextInput(attrs={'class': 'form-control'}),
            'creador': forms.Select(attrs={'class': 'form-control'}),
            'productos': forms.widgets.CheckboxSelectMultiple(),
            'cantidad_productos': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_comprados': forms.TextInput(attrs={'class': 'form-control'}),
            'presupuesto_total': forms.TextInput(attrs={'class': 'form-control'}),
            'total_final': forms.TextInput(attrs={'class': 'form-control'}),
        }
