from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from animais.models import Animal
# Create your views here.
def index(request):
    context = {'caracteristicas': None}
    #if the 'buscar' field is in  the request
    if 'buscar' in request.GET:
        animais= Animal.objects.all()
        animal_persquisado = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains=animal_persquisado)
        context ={'caracteristicas':caracteristicas}
    return render(request, 'index.html', context)