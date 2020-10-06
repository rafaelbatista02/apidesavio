from rest_framework import routers
from Voluntarios.views import *
from django.contrib import admin
from django.urls import path, include

rota = routers.DefaultRouter()
rota.register('voluntario', VoluntirioViewSet)
rota.register('estado', EstadoViewSet)
rota.register('cidade', CidadeViewSet)
rota.register('cidade2', Cidade2ViewSet)






urlpatterns = [
    path('api/', include(rota.urls)),
    path('admin/', admin.site.urls),
    path(r'chaining/', include('smart_selects.urls')),
   
]
