from django.test import TestCase

class TestPaginaInicial(TestCase):
    def test_pagina_inicial_renderiza_html_correto(self):
        response = self.client.get('')
        self.assertIn('<title>Lista de Tarefas</title>', response.content.decode())
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertTrue(response.content.decode().endswith('</html>'))
