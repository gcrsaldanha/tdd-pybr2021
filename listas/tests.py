from django.test import TestCase

class TestPaginaInicial(TestCase):
    def test_pagina_inicial_renderiza_html_correto(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'pagina_inicial.html')

    def test_recebe_post_request(self):
        response = self.client.post('', {'texto_novo_item': 'Comprar livro TDD'})
        self.assertIn('Comprar livro TDD', response.content.decode())
