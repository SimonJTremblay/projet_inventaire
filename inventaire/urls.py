from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventaire-home'),
    path('about/', views.about, name='inventaire-about'),
]