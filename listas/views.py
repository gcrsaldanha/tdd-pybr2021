from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def pagina_inicial(request: HttpRequest):
    if request.method == 'POST':
        texto_novo_item = request.POST['texto_novo_item']
        return render(
            request=request,
            template_name='pagina_inicial.html',
            context={'texto_novo_item': texto_novo_item},
        )
    return render(request=request, template_name='pagina_inicial.html')
