from django.shortcuts import render
from rest_framework import viewsets
from Voluntarios.models import *
from Voluntarios.serializers import *


class VoluntirioViewSet(viewsets.ModelViewSet):
    queryset = Voluntirio.objects.all()
    serializer_class = VoluntirioSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer 

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class Cidade2ViewSet(viewsets.ModelViewSet):
    queryset = Cidade2.objects.all()
    serializer_class = Cidade2Serializer

              

