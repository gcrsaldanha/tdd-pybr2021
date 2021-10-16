from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Caso browser = webdriver.Chrome() não funcione
'''
options = Options()
# binary_location: Executable Path, pode ser consultado em chrome://version
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

browser = webdriver.Chrome(
    executable_path='./venv/bin/chromedriver',
    options=options,
)
'''

browser = webdriver.Chrome()
browser.get('http://google.com')
consulta = browser.find_element_by_name('q')

from selenium.webdriver.common.keys import Keys
consulta.send_keys('python brasil 2021')
consulta.send_keys(Keys.ENTER)