from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('coches-vendidos/', views.Listar_Coches_Vendidos.as_view(), name='listar_coches_vendidos'), # clase PruebaView del archivo views.py
    path('revisiones/', views.Listar_Revisiones.as_view(), name='listar_revisiones')
]