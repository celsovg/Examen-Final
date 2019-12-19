from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .forms import ProductoForm, ListaDeComprasForm
from apps.usuario.forms import RegistroUsuarioForm
from apps.usuario.models import RegistroUsuario
from apps.tienda.models import Tienda
from .models import ListaDeCompras
from django.views.generic import ListView, CreateView

from rest_framework import generics
from .serializers import ProductoSerializer
from .models import Producto

class API_objects(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Create your views here.


def index_compras(request):
    return render(request, 'base/principal.html')

# Views de los productos


def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listarCompras:listar_listas')
    else:
        form = ProductoForm()
    return render(request, 'listaCompras/producto_form.html', {'form': form})


def producto_list(request):
    producto = Producto.objects.all().order_by('id')
    contexto = {'productos': producto}
    return render(request, 'listaCompras/producto_list.html', contexto)


def producto_edit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('listarCompras:listar_producto')
    return render(request, 'listaCompras/producto_form.html', {'form': form})


def producto_delete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarCompras:listar_producto')
    return render(request, 'listaCompras/producto_delete.html', {'producto': producto})

# VIews de las listas


def listados_crear(request):
    if request.method == 'POST':
        form = ListaDeComprasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listarCompras:listar_listas')
    else:
        form = ListaDeComprasForm()
    return render(request, 'listaCompras/listado_form.html', {'form': form})


def listados_list(request):
    lista = ListaDeCompras.objects.all().order_by('id')
    contexto = {'listas': lista}
    paginate_by = 2
    return render(request, 'listaCompras/listado_list.html', contexto)
    


def listados_edit(request, id_lista):
    lista = ListaDeCompras.objects.get(id=id_lista)
    if request.method == 'GET':
        form = ListaDeComprasForm(instance=lista)
    else:
        form = ListaDeComprasForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
        return redirect('listarCompras:listar_listas')

    return render(request, 'listaCompras/listado_form.html', {'form': form})


def listados_delete(request, id_lista):
    lista = ListaDeCompras.objects.get(id=id_lista)
    if request.method == 'POST':
        lista.delete()
        return redirect('listarCompras:listar_listas')
    return render(request, 'listaCompras/listado_delete.html', {'lista': lista})


# Views de CRUDS con dobles vaina

class SolicitudList(ListView):
    model = ListaDeCompras
    template_name = 'listaCompras/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = ListaDeCompras
    template_name = 'listaCompras/solicitud_form.html'
    form_class = ListaDeComprasForm
    second_form_class = ProductoForm
    success_url = reverse_lazy('listaCompras:solicitus_listar')

    def get_context_data(self, **kwargs):

        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.objects = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.listaCompras = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
