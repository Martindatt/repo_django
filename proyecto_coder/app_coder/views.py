from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
# Create your views here.

def curso (request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantillas = loader.get_template("plantillas.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=287318)
    curso.save()
    texto = f"se guardo en la base de datos el Curso: {curso.nombre} Camada:{curso.camada}"
    return HttpResponse (texto)

