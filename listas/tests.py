from django.test import TestCase

class TestPaginaInicial(TestCase):
    def test_pagina_inicial_renderiza_html_correto(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'pagina_inicial.html')
