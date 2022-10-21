from urllib import response
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.factory=RequestFactory()
        self.animal=Animal.objects.create(
            nome_animal='papagaio',
            predador= 'Não',
            venenoso='Não',
            domestico='Sim'
        )

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """teste que verifica se a index retorna as caracteristicas dos animais"""
        response= self.client.get('/', 
            {'buscar':'papagaio'}
        )
        caracteristica_animal_pesquisado= response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'papagaio')
