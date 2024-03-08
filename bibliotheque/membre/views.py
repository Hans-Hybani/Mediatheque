from django.shortcuts import render
from bibliotecaire.models import livre
from bibliotecaire.models import dvd
from bibliotecaire.models import cd
from bibliotecaire.models import jeuDePlateau

def media(request):
        livres = livre.objects.all()
        dvdd =  dvd.objects.all()
        cdd = cd.objects.all()
        jeu = jeuDePlateau.objects.all()
        return render(request,
        './mediaMembre.html',
        {'livres':livres,
        'dvdd':dvdd,
        'cdd':cdd,
        'jeu':jeu},)