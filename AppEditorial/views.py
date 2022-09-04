from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppEditorial.forms import LibrosFormulario, RevistasFormulario

# Mis views aquí

def inicio(request):
    return render(request, "AppEditorial/inicio.html")
    
def libros(request):
    return render(request, "AppEditorial/libros.html")

def revistas(request):
    return render(request, "AppEditorial/revistas.html")

def albumes(request):
    return render(request, "AppEditorial/albumes.html")


# FORMULARIO DE CARGA LIBROS    

def librosFormulario(request):
    
    if request.method=="POST":
        miFormulario=LibrosFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            titulo=info.get("titulo")
            autor=info.get("autor") 
            cant_paginas=info.get("cant_paginas") 
            libro=Libros(titulo=titulo,autor=autor,cant_paginas=cant_paginas)
            libro.save()
            return render(request, "AppEditorial/inicio.html", {"mensaje": "Libro Guardado"})
        else:
            return render (request,"AppEditorial/LibrosFormulario.html", {"mensaje": "Error"}) #51.36
        
    else:
        miFormulario=LibrosFormulario()
        return render(request,"AppEditorial/LibrosFormulario.html", {"formulario":miFormulario})

# FORMULARIO DE CARGA REVISTAS    

def revistasFormulario(request):
    
    if request.method=="POST":
        form=RevistasFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            tema=info.get("tema")
            numero=info.get("numero") 
            cant_paginas=info.get("cant_paginas") 
            revista=Revistas(tema=tema,numero=numero,cant_paginas=cant_paginas)
            revista.save()
            return render(request, "AppEditorial/inicio.html", {"mensaje": "Revista Guardada"})
        else:
            return render (request,"AppEditorial/LibrosFormulario.html", {"mensaje": "Error"}) #51.36
        
    else:
        form=RevistasFormulario()
        return render(request,"AppEditorial/revistasFormulario.html", {"formulario":form})  
    
 
# FORMULARIOS PARA BÚSQUEDA EN BD
# --------------------------Esta vista será para buscar un libro por su autor
def busquedaAutor(request):
    return render(request, "AppEditorial/busquedaAutor.html")

# Esta vista será para mostrar los resultados de la búsqueda
def resultado_busqueda(request):
    if request.GET["autor"]:
        autor=request.GET["autor"]
        autor=Libros.objects.filter(autor=autor) #creo variable, que del modelo Libros filtrará por autor en la base de datos
        if len(autor)!=0:
            return render (request, "AppEditorial/resultado_busqueda.html", {"autor": autor})
        else:
            return render (request, "AppEditorial/resultado_busqueda.html", {"mensaje": "No hay libros cargados de ese autor. Ingrese otro por favor"})
    else:
        return render (request, "AppEditorial/resultado_busqueda.html", {"mensaje": "No enviaste datos"})
    
    
#---------------------------------------Esta vista será para buscar una revista por su año

    
    