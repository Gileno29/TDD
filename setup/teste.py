from cgi import test
from select import select
from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/gileno/Documents/estudando/TDD/chromedriver")
    def tearDown(self):
        self.browser.quit()

    def test_para_verificar_se_a_janela_do_browser_esta_abrindo(self):
        self.browser.get(self.live_server_url)

    def test_deu_ruim(self):
        """Teste de exemplo de erro"""
        self.fail('teste falhou  deu ruim mesmo')
