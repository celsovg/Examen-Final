from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .forms import RegistroTiendaForm
from .models import Tienda


# Create your views here.
def tienda_create(request):
    if request.method == 'POST':
        form = RegistroTiendaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tienda:listar_tienda')
    else:
        form = RegistroTiendaForm()
    return render(request, 'tienda/tienda_form.html', {'form': form})


def tienda_list(request):
    tienda = Tienda.objects.all().order_by('id')
    contexto = {'tiendas': tienda}
    return render(request, 'tienda/tienda_list.html', contexto)


def tienda_edit(request, id_tienda):
    tienda = Tienda.objects.get(id=id_tienda)
    if request.method == 'GET':
        form = RegistroTiendaForm(instance=tienda)
    else:
        form = RegistroTiendaForm(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
        return redirect('tienda:listar_tienda')
    return render(request, 'tienda/tienda_form.html', {'form': form})


def tienda_delete(request, id_tienda):
    tienda = Tienda.objects.get(id=id_tienda)
    if request.method == 'POST':
        tienda.delete()
        return redirect('tienda:listar_tienda')
    return render(request, 'tienda/tienda_delete.html', {'tienda': tienda})