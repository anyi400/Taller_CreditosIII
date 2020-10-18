from django.shortcuts import render
from .models import Coches_Vendidos, Revisiones

from django.views.generic import ListView, CreateView

# Create your views here.

class Listar_Coches_Vendidos(ListView):
    template_name = "cochesVendidos/listar_coches_vendidos.html"
    model=Coches_Vendidos
    context_object_name='lista'


class Listar_Revisiones(ListView):
    template_name = "revisiones/listar_revisiones.html"
    model=Revisiones
    context_object_name='lista'