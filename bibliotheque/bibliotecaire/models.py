from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Media(models.Model):
    name = models.CharField(max_length=45)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class livre(Media):
    auteur = models.CharField(max_length=45)

class dvd(Media):
    realisateur = models.CharField(max_length=45)

class cd(Media):
    artiste = models.CharField(max_length=45)

class jeuDePlateau(models.Model):
    name = models.CharField(max_length=45)
    createur = models.CharField(max_length=45)

class emprunteur(models.Model):
    #l'utilisation de la nommenclature emprunteur au lieu de Membre m'a juste aidé pour poursuivre ma logique d'emprun de média/ choix personnel
    nom = models.CharField(max_length=45)
    bloque = models.BooleanField(default=False)
    nb_emprunts = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nom
