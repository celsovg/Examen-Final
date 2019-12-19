from django.conf.urls import include, url
from django.urls import path
from .views import tienda_create, tienda_list, tienda_edit, tienda_delete

app_name = 'tienda'

urlpatterns = [
    url(r'^crear$', tienda_create, name='crear_tienda'),
    url(r'^listar$', tienda_list, name='listar_tienda'),
    url(r'^editar/(?P<id_tienda>\d+)$', tienda_edit, name='editar_tienda'),
    url(r'^eliminar/(?P<id_tienda>\d+)$', tienda_delete, name='eliminar_tienda'),


]    