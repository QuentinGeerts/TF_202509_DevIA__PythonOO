# Exercice 01

# Reprenez la démonstration 01 (demo01-classes).
# Créer une classe Propriétaire qui est caractérisée par :
# - Un nom (chaîne de caractères)
# - Un prénom (chaîne de caractères)
# - Une date de naissance (Date seulement (Read The Fucking Manual))

# La classe possède également un comportement qui permet d'afficher les informations du propriétaire.

# Ajouter à la classe Voiture, un propriétaire.

# Testez les modifications et ajouts dans les blocs de tests.

# Dans le programme principal, importez vos classes et créez :

# - Propriétaire 1: Geerts Quentin 03/04/1996 
# - Propriétaire 2: Adams Michel 01/01/1980


# - Voiture 1: Kia Ceed Quentin
# - Voiture 2: Volkswaggen Polo Michel

# from models.proprietaire import Proprietaire
# from models.voiture import Voiture
# from models import proprietaire as p, voiture as v

from models import Proprietaire, Voiture
from datetime import date

# Création des propriétaires
proprietaire1: Proprietaire = Proprietaire()
proprietaire1.nom = "Geerts"
proprietaire1.prenom = "Quentin"
proprietaire1.date_naissance = date(1996, 4, 3)

proprietaire2: Proprietaire = Proprietaire()
proprietaire2.nom = "Adams"
proprietaire2.prenom = "Michel"
proprietaire2.date_naissance = date(1980, 1, 1)

print(proprietaire1)
print(proprietaire2.__str__())

# Création des voitures
voiture1: Voiture = Voiture()
voiture1.marque = "Kia"
voiture1.modele = "Ceed"
voiture1.proprietaire = proprietaire1

voiture2: Voiture = Voiture()
voiture2.marque = "Volkswaggen"
voiture2.modele = "Polo"
voiture2.proprietaire = proprietaire2

print(voiture1)
print(voiture2)
