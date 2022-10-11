from select import select
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/gileno/Documents/estudando/TDD/chromedriver")
    def tearDown(self):
        self.browser.quit()
  

    def test_buscando_um_novo_animal(self):
        """
            Teste se um usuário encontra um animal na pesquisa
        """
        self.browser.get(self.live_server_url + '/')
        brand_element  = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        pass

    
    #find_element(By.CSS_SELECTOR, 'exemplo')