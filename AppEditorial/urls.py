from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('Libros', libros, name="libros"),
    path('Revistas', revistas, name="revistas"),
    path('Albumes', albumes, name="albumes"),
    path('LibrosFomulario', librosFormulario, name="librosFormulario"),
    path('RevistasFomulario', revistasFormulario, name="revistasFormulario"),
    path('busquedaAutor', busquedaAutor, name="busquedaAutor"),
    path('resultado_busqueda', resultado_busqueda, name="resultado_busqueda"),

    
    
]