from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppKeepCoding.models import Curso


def curso(self):
    curso = Curso(nombre="Java", camada=19882)
    curso.save()
    texto = f"Curso: {curso.nombre}, Camada: {curso.camada}"
    return HttpResponse(texto)