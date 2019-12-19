import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistroUsuarioForm, RegistroForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.views.generic import TemplateView

from rest_framework.views import APIView
from apps.usuario.serializer import UserSerializer

# Create your views here.


def index_usuario(request):
    return render(request, 'base/base.html')


def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuario:index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuario/usuario_form.html', {'form': form})


class RegistroUsuario (CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('listarCompras:listar_listas')


def usuario_login(request):
    # Valida si existe un usuario autenticado
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse, ('usuario:login'))
    else:
        # Recibe formulario mediante metodo POST
        if request.method == 'POST':
            # Recibimos la informacion del formulario
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Autenticamos el usuario
            user = authenticate(username=username, password=password)
            # Verifica que exista el usuario
            if user:
                # Verifica si el usuario esta activo
                if user.is_active:
                    # Genera un login para autenticar al usuario
                    login(request, user)
                    return HttpResponseRedirect(reverse('usuario:login'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva.")
            else:
                # Si no existe usuario
                print("username: {} - password: {}".format(username, password))
                return HttpResponse("Datos inválidos")
        else:  # Si llega desde una url en metodo GET (desde el navegador)
            return render(request, 'usuario/index_usuario.html', {})
# -----------  FIN SEISON --------------------



class IndexView(TemplateView):
    template_name = 'usuario/index_usuario.html'


class UserAPI(APIView):
    serializer = UserSerializer
    
    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')