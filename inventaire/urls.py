from django.urls import path
from .views import (
    ProduitListView,
    ProduitDetailView,
    ProduitCreateView,
    ProduitUpdateView,
    ProduitDeleteView,
)
from . import views

urlpatterns = [
    path('', ProduitListView.as_view(), name='inventaire-home'),
    path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('produit/new/', ProduitCreateView.as_view(), name='produit-create'),
    path('produit/<int:pk>/update/', ProduitUpdateView.as_view(), name='produit-update'),
    path('produit/<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit-delete'),
    path('about/', views.about, name='inventaire-about'),
]
