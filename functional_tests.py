from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Lista de Tarefas' in browser.title, f'browser.title: {browser.title}'