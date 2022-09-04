from django.db import models

class Libros(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    cant_paginas=models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo+" - "+str(self.autor)
    
class Revistas(models.Model):
    tema=models.CharField(max_length=50, default='SOME STRING')
    numero=models.CharField(max_length=50)
    cant_paginas=models.CharField(max_length=50)   
        
class Albumes(models.Model):
    tematica=models.CharField(max_length=50)
    cant_figuritas_total=models.CharField(max_length=50)
    
