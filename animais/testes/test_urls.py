from urllib import request, response
from django.test import RequestFactory, TestCase
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory= RequestFactory()
   
    def test_validacacao_usabilidade_index(self):
        """Testa se a home da aplicação utiliza a função index da view"""
        request=self.factory.get('/')
        with self.assertTemplateUsed('index.html'):

            response=index(request)
        
            self.assertEqual(response.status_code, 200)