from django.test import TestCase
from .models import Tarefa


class TestPaginaInicial(TestCase):
    def test_pagina_inicial_renderiza_html_correto(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'pagina_inicial.html')

    def test_recebe_post_request(self):
        response = self.client.post(
            '', {'texto_novo_item': 'Comprar livro TDD'})
        self.assertIn('Comprar livro TDD', response.content.decode())

    def test_salva_tarefa_no_banco_de_dados(self):
        self.client.post('/', {'texto_novo_item': 'Comprar livro de TDD'})
        self.assertEqual(Tarefa.objects.count(), 1)

        tarefa_db = Tarefa.objects.get()
        self.assertEqual(tarefa_db.texto, 'Comprar livro de TDD')


class TestTarefaModel(TestCase):
    def test_cria_nova_tarefa_no_banco_de_dados(self):
        tarefa = Tarefa()
        tarefa.texto = 'Comprar livro de TDD'
        tarefa.save()  # atribui um ID

        tarefa_db = Tarefa.objects.get(id=tarefa.id)
        self.assertEqual(tarefa_db.texto, 'Comprar livro de TDD')
