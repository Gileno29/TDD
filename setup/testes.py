from select import select
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


'''
    testes fncionais são baseados em user historys podem ser realizados
    de forma manual ou atrás de ajuda de frameworks e bibliotecas
    nesse caso foi o usado o framwork de testes do django que é contruido na
    padrão unnitest
'''
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
        


        buscar_animal_input= self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão') 
       

       #Ele pesquisa por Leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        time.sleep(2)
        self.browser.find_element_by_css_selector('form button').click()
        time.sleep(2)

        #O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements_by_css_selector(".result-description")
        self.assertGreater(len(caracteristicas), 3)

        #Ele desiste de adotar um leão

    #find_element(By.CSS_SELECTOR, 'exemplo')