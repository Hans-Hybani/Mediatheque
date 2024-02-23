"""
URL configuration for bibliotheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bibliotecaire import views as bibliotecaire_views
from membre import views as membre_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bibliotecaire_views.menu_bibliotheque),
    path('menu_bibliotheque/', bibliotecaire_views.menu_bibliotheque),
    path('biblio_media/', bibliotecaire_views.media),
    path('membre_media/', membre_views.media),
    path('ajoutlivre/', bibliotecaire_views.ajoutLivre),
    path('ajoutdvd/', bibliotecaire_views.ajoutdvd),
    path('ajoutcd/', bibliotecaire_views.ajoutcd),
    path('ajoutjeu/', bibliotecaire_views.ajoutjeu),
    path('list_emprunt/', bibliotecaire_views.Emprunteur),
    path('ajout_Emprunt/', bibliotecaire_views.ajoutemprunt),
    path('delete/<int:id>/', bibliotecaire_views.delete),
    path('modifier_emprunteur/<int:id>/', bibliotecaire_views.updateEmprunteur),
    path('selection_emprunteur_livre/<int:media_id>/', bibliotecaire_views.selection_emprunteur_livre),
    path('selection_emprunteur_cd/<int:media_id>/', bibliotecaire_views.selection_emprunteur_cd),
    path('selection_emprunteur_dvd/<int:media_id>/', bibliotecaire_views.selection_emprunteur_dvd),
    path('attribuer_emprunt_livre/<int:livre_id>/', bibliotecaire_views.attribuer_emprunt_livre, name='attribuer_emprunt_livre'),
    path('attribuer_emprunt_cd/<int:cd_id>/', bibliotecaire_views.attribuer_emprunt_cd, name='attribuer_emprunt_cd'),
    path('attribuer_emprunt_dvd/<int:dvd_id>/', bibliotecaire_views.attribuer_emprunt_dvd, name='attribuer_emprunt_dvd'),
    path('accueil_bibliotecaire/', bibliotecaire_views.acceuilBibliotecaire),
    path('retourbibliomedia/', bibliotecaire_views.retourbibliomedia),
    path('emprunt/', bibliotecaire_views.emprunt_voir),
    path('menu_membre/', membre_views.media),
    path('bibliotheque/login/', bibliotecaire_views.bibliotheque_login, name='bibliotheque_login'),
    path('membre/login/', bibliotecaire_views.membre_login, name='membre_login'),
]
