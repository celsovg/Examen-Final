from django.urls import path, include
from django.conf.urls import url
from .views import registro_view, index_usuario, RegistroUsuario, usuario_login, UserAPI
app_name = 'usuario'

urlpatterns = [
    url(r'^index$', index_usuario, name='index'),
    url(r'^registrar$', RegistroUsuario.as_view(), name='registrar'),
    url(r'^login$', usuario_login , name='login'),
    url(r'^api$', UserAPI.as_view() , name='api'),

]
