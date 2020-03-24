from django.shortcuts import render
from .models import Produit


def home(request):
    """ renders inventaire/home.html"""
    context = {
        'produits': Produit.objects.all()
    }
    return render(request, 'inventaire/home.html', context)

def about(request):
    return render(request, 'inventaire/about.html', {'title': 'About'})

