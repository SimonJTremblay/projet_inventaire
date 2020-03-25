from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Produit
from django.db.models import F


def home(request):
    """ renders inventaire/home.html"""
    context = {
        'produits': Produit.objects.all()
    }
    return render(request, 'inventaire/home.html', context)

class ProduitListView(ListView):
    model = Produit
    context_object_name = 'produits'
    ordering = ['Nom']
    # class-based view, by default, are looking in this path
    # <app>/<model>_<viewtype>.hmtl
    template_name = 'inventaire/home.html'

class ProduitDetailView(LoginRequiredMixin, DetailView):
    model = Produit
    # <app>/<model>_<viewtype>.hmtl
    # inventaire/produit_detail.html

class ProduitCreateView(LoginRequiredMixin, CreateView):
    model = Produit
    fields = ['Nom', 'Description', 'Type', 'QuantiteStock']

class ProduitUpdateView(LoginRequiredMixin, UpdateView):
    model = Produit
    fields = ['Nom', 'Description', 'Type', 'QuantiteStock', 'SeuilMinimum']

class ProduitDeleteView(LoginRequiredMixin, DeleteView):
    model = Produit
    success_url = '/'

class AchatProduitListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    queryset = Produit.objects.filter(QuantiteStock__lte=F('SeuilMinimum'))
    context_object_name = 'produits'
    ordering = ['-QuantiteStock']
    permission_required = 'is_superuser'
    template_name = 'inventaire/produit-achat.html'


def about(request):
    return render(request, 'inventaire/about.html', {'title': 'About'})

