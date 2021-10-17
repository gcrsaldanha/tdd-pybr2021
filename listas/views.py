from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def pagina_inicial(request: HttpRequest):
    return HttpResponse('<html><title>Lista de Tarefas</title></html>')
