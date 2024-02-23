from django import forms

class Creationlivre(forms.Form):
      name = forms.CharField(required=False)
      auteur = forms.CharField(required=False)
      dateEmprunt = forms.DateField(required=False)
      disponible = forms.BooleanField(required=False)

class Creationdvd(forms.Form):
      name = forms.CharField(required=False)
      realisateur = forms.CharField(required=False)
      dateEmprunt = forms.DateField(required=False)
      disponible = forms.BooleanField(required=False)

class Creationcd(forms.Form):
      name = forms.CharField(required=False)
      artiste = forms.CharField(required=False)
      dateEmprunt = forms.DateField(required=False)
      disponible = forms.BooleanField(required=False)

class Creationjeu(forms.Form):
      name = forms.CharField(required=False)
      createur = forms.CharField(required=False)

class Creationemprunteur(forms.Form):
      nom = forms.CharField(required=False)
      bloque = forms.BooleanField(required=False)

class Updateemprunteur(forms.Form):
      nom = forms.CharField(required=False)
      bloque = forms.BooleanField(required=False)
      
class BibliothequeLoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class MembreLoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)