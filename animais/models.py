from django.db import models

# Create your models here.

class Animal(models.Model):
    nome_animal= models.CharField(max_length=20, blank=True)
    predador= models.CharField(max_length=5, blank=True)
    venenoso= models.CharField(max_length=5, blank=True)
    domestico=models.CharField(max_length=5, blank=True)


    def __str__(self):
        return self.nome_animal