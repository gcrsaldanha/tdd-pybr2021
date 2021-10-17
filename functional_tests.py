import unittest
from selenium import webdriver


class TestPaginaInicial(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_pagina_inicial(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Lista de Tarefas', self.browser.title)


if __name__ == '__main__':
    unittest.main()