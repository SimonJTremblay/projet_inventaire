from django.shortcuts import render


produits = [
    {
        'Nom': 'clous - 1\"',
        'Description': 'boite de 20 clous de 1\"',
        'Type': 'materiel',
        'QuantiteStock': '200',
        'SeuilMinimum': '50',
    },
    {
        'Nom': 'vis - 1\"',
        'Description': 'boite de 30 vis de 1\"',
        'Type': 'materiel',
        'QuantiteStock': '125',
        'SeuilMinimum': '50',
    }
]

def home(request):
    context = {
        'produits': produits
    }
    return render(request, 'inventaire/home.html', context)

def about(request):
    return render(request, 'inventaire/about.html', {'title': 'About'})

