from django.shortcuts import render
from django.http import HttpResponse
from bibliotecaire.models import livre
from bibliotecaire.models import dvd
from bibliotecaire.models import cd
from bibliotecaire.models import jeuDePlateau

def menu_membre(request):
        return HttpResponse('<h1>Hello Django!</h1>')


def menuMembre():
        print("c'est le menu de l'application des membres")
        print("affiche tout")

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