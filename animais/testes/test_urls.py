from django.test import TestCase
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):
    """Testa se a home da aplicação utiliza a função index da view"""
    def test_rota_url_utiliza_view_idex(self):
        root = reverse('/')
        self.assertEqual(root.func, index)