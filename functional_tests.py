import unittest
from selenium import webdriver


class TestPaginaInicial(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_pagina_inicial(self):
        # Maria ouviu falar de um novo site de lista de tarefas (To-Do Lists)
        # Ela acessa a página inicial e vê "Lista de Tarefas"
        self.browser.get('http://localhost:8000')
        self.assertIn('Lista de Tarefas', self.browser.title)
        # Ela percebe que há um cabeçalho escrito "Tarefas".

        # Abaixo deste cabeçalho, há um campo em branco (input field)
        # para inserir uma nova tarefa.

        # Ela digita "Comprar livro de TDD"

        # Ao apertar enter, um novo item numerado aparece na lista

        # Maria então adiciona uma nova tarefa: "Terminar palestra de Pyhton" (numerada como 2).
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


if __name__ == '__main__':
    unittest.main()
