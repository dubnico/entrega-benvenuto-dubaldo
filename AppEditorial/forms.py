from django import forms 


class LibrosFormulario(forms.Form):
    titulo=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=50)
    cant_paginas=forms.CharField(max_length=50)
    
class RevistasFormulario(forms.Form):
    tema=forms.CharField(max_length=50)
    numero=forms.CharField(max_length=50)
    cant_paginas=forms.CharField(max_length=50)    