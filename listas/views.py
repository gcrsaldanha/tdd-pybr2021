from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Tarefa

def pagina_inicial(request: HttpRequest):
    if request.method == 'POST':
        texto_novo_item = request.POST['texto_novo_item']
        tarefa = Tarefa()
        tarefa.texto = texto_novo_item
        tarefa.save()

    tarefas = Tarefa.objects.all()
    return render(
        request=request,
        template_name='pagina_inicial.html',
        context={'tarefas': tarefas}
    )
