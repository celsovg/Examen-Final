from django.conf.urls import include, url
from django.urls import path
from .views import index_compras, producto_crear, producto_list, producto_edit, producto_delete
from .views import listados_list, listados_crear, listados_edit, listados_delete
from .views import SolicitudList, SolicitudCreate
from .views import API_objects, API_objects_details
app_name = 'listarCompras'

urlpatterns = [

    #URLS de los productos
    url(r'^$', index_compras, name='index'),
    url(r'^nuevoproducto$', producto_crear, name='crear_producto'),
    url(r'^listarproducto', producto_list, name='listar_producto'),
    url(r'^editarproducto/(?P<id_producto>\d+)$', producto_edit, name='editar_producto'),
    url(r'^eliminarproducto/(?P<id_producto>\d+)$', producto_delete, name='eliminar_producto'),
    #URLS de las listas
    url(r'^listalistados$', listados_list, name='listar_listas'),
    url(r'^nuevolistado$', listados_crear, name='crear_listas'),
    url(r'^editarlistado/(?P<id_lista>\d+)$', listados_edit, name='editar_listas'),
    url(r'^eliminarlistado/(?P<id_lista>\d+)$', listados_delete, name='eliminar_listas'),

    #Otras URLS
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nuevo$', SolicitudCreate.as_view(), name='solicitud_crear'),
    #URL del Serializers
    path('basic/', API_objects.as_view()),
    path('basic/<int:pk>/', API_objects_details.as_view()),

]
