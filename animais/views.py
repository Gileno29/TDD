from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import animais
from animais.models import Animal
# Create your views here.
def index(request):
    context = {'caracteristicas': Animal.objects.all()}
    return render(request, 'index.html', context)