import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPaginaInicial(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_pagina_inicial(self):
        # Maria ouviu falar de um novo site de lista de tarefas (To-Do Lists)
        # Ela acessa a página inicial e vê "Lista de Tarefas"
        self.browser.get(self.live_server_url)
        self.assertIn('Lista de Tarefas', self.browser.title)

        # Ela percebe que há um cabeçalho escrito "Tarefas".
        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn(h1.text, 'Tarefas')

        # Abaixo deste cabeçalho, há um campo em branco (input field)
        # para inserir uma nova tarefa.
        input_field = self.browser.find_element_by_id('id_novo_item')

        # Ela digita "Comprar livro de TDD"
        input_field.send_keys('Comprar livro de TDD')

        # Ao apertar enter, um novo item numerado aparece na lista
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)
        tabela = self.browser.find_element_by_tag_name('table')
        rows = tabela.find_elements_by_tag_name('tr')
        self.assertIn(
            '1: Comprar livro de TDD',
            rows[0].text,
        )

        # Maria então adiciona uma nova tarefa: "Terminar palestra de Python" (numerada como 2).
        input_field = self.browser.find_element_by_id('id_novo_item')
        input_field.send_keys('Terminar palestra de Python')
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)
        tabela = self.browser.find_element_by_tag_name('table')
        rows = tabela.find_elements_by_tag_name('tr')
        self.assertIn(
            '2: Terminar palestra de Python',
            rows[1].text,
        )

        # Maria percebe que ao lado de cada tarefa há 3 opções (indicadas por ícones):
        # - Concluir
        # - Excluir
        # - Editar

        # Maria então resolve concluir a sua primeira tarefa clicando no respectivo item.
        # A tarefa aparece riscada e na última posição na lista sem um número
        # (separada por uma barra horizontal das tarefas não-concluídas).
        # A tarefa restante (originalmente numerada como 2) assume a primeira posição (numerada como 1).

        # Percebendo um erro na tarefa 1 ("Terminar palestra the Pyhton", Maria resolve editá-la.
        # O input field é populado com o texto da tarefa e Maria consegue atualizá-la.

        # Maria, por fim, decide excluir a tarefa 1. Ao fazer isso, a tarefa excluída some.
