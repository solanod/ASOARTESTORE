from multiprocessing import context
from django.shortcuts import render
from django.template import Template, Context 

# Create your views here.

def usuarios(request):
    context = {
        
    }
    return render(request, 'usuarios/usuarios.html', context)
