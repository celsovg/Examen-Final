
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.usuario.views import IndexView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('listas/', include('apps.listaCompras.urls')),
    path('usuarios/', include('apps.usuario.urls')),
    path('tienda/', include('apps.tienda.urls')),
    path('',include('apps.listaCompras.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    url(r'^faceook$', IndexView.as_view()),

]
