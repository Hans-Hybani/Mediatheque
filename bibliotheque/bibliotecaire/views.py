from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from bibliotecaire.models import livre
from bibliotecaire.models import dvd
from bibliotecaire.models import cd
from bibliotecaire.models import jeuDePlateau
from bibliotecaire.models import emprunteur
from bibliotecaire.form import Creationlivre
from bibliotecaire.form import Creationdvd
from bibliotecaire.form import Creationcd
from bibliotecaire.form import Creationjeu
from bibliotecaire.form import Creationemprunteur
from bibliotecaire.form import Updateemprunteur
from bibliotecaire.form import BibliothequeLoginForm
from bibliotecaire.form import MembreLoginForm

def menu_bibliotheque(request):
        livres = livre.objects.all()
        dvdd =  dvd.objects.all()
        cdd = cd.objects.all()
        jeu = jeuDePlateau.objects.all()
        emprun = emprunteur.objects.all()
        return render(request,
        './menuBiblio.html',
        {'livres':livres,
        'dvdd':dvdd,
        'cdd':cdd,
        'jeu':jeu,
        'emprun':emprun},)

def media(request):
        livres = livre.objects.all()
        dvdd =  dvd.objects.all()
        cdd = cd.objects.all()
        jeu = jeuDePlateau.objects.all()
        emprun = emprunteur.objects.all()
        return render(request,
        './media.html',
        {'livres':livres,
        'dvdd':dvdd,
        'cdd':cdd,
        'jeu':jeu,
        'emprun':emprun},)

def Emprunteur(request):
        emprun = emprunteur.objects.all()
        return render(request,
        './listemprunteur.html',
        {'emprun':emprun},)

def ajoutLivre(request):
    if request.method == 'POST':
        creationlivre = Creationlivre(request.POST)
        if creationlivre.is_valid():
            livree = livre()
            livree.name = creationlivre.cleaned_data['name']
            livree.auteur = creationlivre.cleaned_data['auteur']
            livree.dateEmprunt = creationlivre.cleaned_data['dateEmprunt']
            livree.disponible = creationlivre.cleaned_data['disponible']
            livree.save()
            livree = livre.objects.all()
            return redirect('/biblio_media/')
        return render(request, './ajoutlivre.html', {'livree': livree})
    else:
        creationlivre = Creationlivre()

    return render(request, './ajoutlivre.html', {'creationLivre': creationlivre})

def ajoutdvd(request):
    if request.method == 'POST':
        creationdvd = Creationdvd(request.POST)
        if creationdvd.is_valid():
            dvvd = dvd()
            dvvd.name = creationdvd.cleaned_data['name']
            dvvd.realisateur = creationdvd.cleaned_data['realisateur']
            dvvd.dateEmprunt = creationdvd.cleaned_data['dateEmprunt']
            dvvd.disponible = creationdvd.cleaned_data['disponible']
            dvvd.save()
            dvvd = dvd.objects.all()
            return redirect('/biblio_media/')
        return render(request, './ajoutdvd.html', {'dvvd': dvvd})
    else:
        creationdvd = Creationdvd()

    return render(request, './ajoutdvd.html', {'creationdvd': creationdvd})

def ajoutcd(request):
    if request.method == 'POST':
        creationcd = Creationcd(request.POST)
        if creationcd.is_valid():
            ccd = cd()
            ccd.name = creationcd.cleaned_data['name']
            ccd.artiste = creationcd.cleaned_data['artiste']
            ccd.dateEmprunt = creationcd.cleaned_data['dateEmprunt']
            ccd.disponible = creationcd.cleaned_data['disponible']
            ccd.save()
            ccd = cd.objects.all()
            return redirect('/biblio_media/')
        return render(request, './ajoutcd.html', {'ccd': ccd})
    else:
        creationcd = Creationcd()

    return render(request, './ajoutcd.html', {'creationcd': creationcd})

def ajoutjeu(request):
    if request.method == 'POST':
        creationjeu = Creationjeu(request.POST)
        if creationjeu.is_valid():
            jeux = jeuDePlateau()
            jeux.name = creationjeu.cleaned_data['name']
            jeux.createur = creationjeu.cleaned_data['createur']
            jeux.save()
            jeux = jeuDePlateau.objects.all()
            return redirect('/biblio_media/')
        return render(request, './ajoutjeu.html', {'jeux': jeux})
    else:
        creationjeu = Creationjeu()

    return render(request, './ajoutjeu.html', {'creationjeu': creationjeu})

def ajoutemprunt(request):
    if request.method == 'POST':
        creationemprunteur  = Creationemprunteur(request.POST)
        if creationemprunteur.is_valid():
            emprunt = emprunteur()
            emprunt.nom = creationemprunteur.cleaned_data['nom']
            emprunt.bloque = creationemprunteur.cleaned_data['bloque']
            emprunt.save()
            return redirect('/list_emprunt/')
        emprunt = emprunteur.objects.all()
        return render(request, './ajoutEmprunt.html', {'emprunt': emprunt})
    else:
        creationemprunteur = Creationemprunteur()

    return render(request, './ajoutEmprunt.html', {'creationemprunteur': creationemprunteur})

def updateEmprunteur(request, id):
    if request.method == 'POST':
        emprunt = emprunteur.objects.get(pk=id)
        update_emprunt = Updateemprunteur(request.POST)
        if update_emprunt.is_valid():
            emprunt.nom = update_emprunt.cleaned_data['nom']
            emprunt.bloque = update_emprunt.cleaned_data['bloque']
            emprunt.save()
            return redirect('/list_emprunt/') 
        emprunt = emprunteur.objects.all()
        return render(request, './modifierEmprunteur.html',{'emprunt': emprunt})
    else:
        update_emprunt = Updateemprunteur()
        return render(request,'./modifierEmprunteur.html',{'update_emprunt': update_emprunt})
    
def delete(request,id):
    emprunt = emprunteur.objects.get(id=id)
    emprunt.delete()
    return redirect('/list_emprunt/')

def selection_emprunteur_livre(request, media_id):
    emprunteurs = emprunteur.objects.all()
    return render(request, './creeEmpruntLivre.html', {'emprunteurs': emprunteurs, 'media_id': media_id, 'livre_id': media_id})

def selection_emprunteur_dvd(request, media_id):
    emprunteurs = emprunteur.objects.all()
    return render(request, './creeEmpruntDvd.html', {'emprunteurs': emprunteurs, 'media_id': media_id, 'dvd_id': media_id})
     
def selection_emprunteur_cd(request, media_id):
    emprunteurs = emprunteur.objects.all()
    return render(request, './creeEmpruntCd.html', {'emprunteurs': emprunteurs, 'media_id': media_id, 'cd_id': media_id})


MAX_EMPRUNTS = 3

def attribuer_emprunt_livre(request, livre_id):
    if request.method == 'POST':
        emprunteur_id = request.POST.get('emprunteur')
        emprunteur_livre_obj = emprunteur.objects.get(pk=emprunteur_id)
        
        # Vérifier si l'emprunteur a déjà atteint le maximum d'emprunts
        if emprunteur_livre_obj.nb_emprunts < MAX_EMPRUNTS:
            # Incrémenter le nombre d'emprunts de l'emprunteur
            emprunteur_livre_obj.nb_emprunts += 1
            emprunteur_livre_obj.save()

            # Effectuer l'emprunt du livre
            livre_obj = livre.objects.get(pk=livre_id)
            livre_obj.emprunteur = emprunteur_livre_obj
            livre_obj.disponible = False
            livre_obj.save()

            return redirect('/biblio_media/')  # Redirection vers la page souhaitée

        # Si l'emprunteur a atteint le maximum d'emprunts, afficher un message d'erreur ou rediriger vers une autre page
        else:
            return HttpResponse("Vous avez déjà atteint le maximum d'emprunts.")

    return render(request, 'creeEmpruntLivre.html')

def attribuer_emprunt_dvd(request, dvd_id):
    if request.method == 'POST':
        emprunteur_id = request.POST.get('emprunteur')
        emprunteur_dvd_obj = emprunteur.objects.get(pk=emprunteur_id)
        
        if emprunteur_dvd_obj.nb_emprunts < MAX_EMPRUNTS:
            emprunteur_dvd_obj.nb_emprunts += 1
            emprunteur_dvd_obj.save()

            dvd_obj = dvd.objects.get(pk=dvd_id)
            dvd_obj.emprunteur = emprunteur_dvd_obj
            dvd_obj.disponible = False
            dvd_obj.save()

            return redirect('/biblio_media/')  

        else:
            return HttpResponse("Vous avez déjà atteint le maximum d'emprunts.")

    return render(request, 'creeEmpruntDvd.html')

def attribuer_emprunt_cd(request, cd_id):
    if request.method == 'POST':
        emprunteur_id = request.POST.get('emprunteur')
        emprunteur_cd_obj = emprunteur.objects.get(pk=emprunteur_id)
        
        if emprunteur_cd_obj.nb_emprunts < MAX_EMPRUNTS:
            emprunteur_cd_obj.nb_emprunts += 1
            emprunteur_cd_obj.save()

            cd_obj = cd.objects.get(pk=cd_id)
            cd_obj.emprunteur = emprunteur_cd_obj
            cd_obj.disponible = False
            cd_obj.save()

            return redirect('/biblio_media/')  

        else:
            return HttpResponse("Vous avez déjà atteint le maximum d'emprunts.")

    return render(request, 'creeEmpruntCd.html')


def emprunt_voir(request):
    emprunteurs = emprunteur.objects.all()
    context = {'emprunteurs': emprunteurs}
    return render(request, './emprunteur.html', context)

def bibliotheque_login(request):
    if request.method == 'POST':
        form = BibliothequeLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Vérifiez si les informations d'identification correspondent aux valeurs attendues
            if username == 'BiBlioTech' and password == 'BiBP@ss1234':
                # Créez une session d'utilisateur fictive
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return render(request,'./bibliotecaire.html')  # Redirection vers la page des bibliothécaires
            # Si les informations d'identification ne correspondent pas, affichez un message d'erreur
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = BibliothequeLoginForm()
    return render(request, 'logBiblio.html', {'form': form})

from django.shortcuts import redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def membre_login(request):
    if request.method == 'POST':
        form = MembreLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Vérifiez si les informations d'identification correspondent aux valeurs attendues
            if username == 'MEmbree' and password == 'mEmp@ss1234':
                # Créez une session d'utilisateur fictive
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('/membre_media/') 
            # Si les informations d'identification ne correspondent pas, on affiche message d'erreur
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = MembreLoginForm()
    return render(request, 'logMembre.html', {'form': form})

def acceuilBibliotecaire(request):
    return render(request, './bibliotecaire.html')

def retourbibliomedia(request):
    return redirect('/biblio_media/')

