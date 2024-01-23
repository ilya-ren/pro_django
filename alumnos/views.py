from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Alumno, Genero 

from .forms import GeneroForm

# Create your views here.
def index(request):
    context={}
    return render(request, 'alumnos/index.html', context)

def crud(request):
    alumnos=Alumno.objects.all()
    context={'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def crud_generos(request):
    generos=Genero.objects.all()
    context={'genero': generos}
    print("Enviando datos a generos_list")
    return render(request,"alumnos/generos_list.html", context)