from django.test import TestCase
from bibliotecaire.models import livre
from bibliotecaire.models import dvd
from bibliotecaire.models import cd
from bibliotecaire.models import jeuDePlateau
from bibliotecaire.models import emprunteur
from datetime import datetime
from django.urls import reverse

class MenuBibliothequeTestCase(TestCase):
    def setUp(self):
        # Création des données de test
        self.livre = livre.objects.create(name='Dragon ball', auteur='akira', dateEmprunt= datetime(2024, 5, 2), disponible=False)
        self.dvd = dvd.objects.create(name='Inception', realisateur='Christopher Nolan', dateEmprunt=datetime(2024, 2, 15), disponible=False)
        self.cd = cd.objects.create(name='Hans HYBANI PRINCIA', artiste='Micheal Jackson', dateEmprunt=datetime(2024, 5, 2), disponible=False)
        self.jeu = jeuDePlateau.objects.create(name='Naruto Plateau', createur='Masashi')
        self.emprun = emprunteur.objects.create(nom='Hans Hybani')

    def test_menu_bibliotheque(self):
        # Exécuter la vue
        response = self.client.get(reverse('menu_bibliotheque'))
        
        # Vérifier que la page a bien répondu avec le code 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Vérifier que les données sont présentes dans le contexte de rendu
        self.assertIn('livres', response.context)
        self.assertIn('dvdd', response.context)
        self.assertIn('cdd', response.context)
        self.assertIn('jeu', response.context)
        self.assertIn('emprun', response.context)
        
        # Vérifier que les données de test sont présentes dans le contexte de rendu
        livres = response.context['livres']
        dvdd = response.context['dvdd']
        cdd = response.context['cdd']
        jeu = response.context['jeu']
        emprun = response.context['emprun']
        
        # Vérifiez que le livres de test sont présents
        self.assertEqual(livres.count(), 1)
        # Vérifiez que le dvd de test sont présents
        self.assertEqual(dvdd.count(), 1)
        # Vérifiez que le cd de test sont présents
        self.assertEqual(cdd.count(), 1)
        # Vérifiez que le jeu de test sont présents
        self.assertEqual(jeu.count(), 1)
        # Vérifiez que l'emprunteur de test sont présents
        self.assertEqual(emprun.count(), 1)

