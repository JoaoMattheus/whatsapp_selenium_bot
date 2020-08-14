from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import path
from os import getcwd

class Efrata:
    pasta = getcwd()
    chromedriver = path.join(pasta, 'drive/chromedriver.exe')
    perfil = path.join(pasta, 'profile', 'wpp')

    def __init__(self):
        self.opcoes = webdriver.ChromeOptions()
        self.opcoes.add_argument(r'user-data-dir={}'.format(self.perfil))
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=self.opcoes)
        self.driver.get('https://web.whatsapp.com/')
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
    
    def ultima_mensagem(self):
        try:
            posts = self.driver.find_elements_by_class_name('_31gEB')
            for post in posts:
                post.click()
                textos = self.driver.find_elements_by_class_name('selectable-text')
                return textos[-2].text
        except:
            pass

efrata = Efrata()
while True:
    msg = efrata.ultima_mensagem()
    if msg:
        print(msg)
        msg = None