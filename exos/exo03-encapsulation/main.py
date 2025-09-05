# Exercice 03 - Encapsulation

# Reprenez la démo 03 (demo03-encapsulation)

# Transformez les différents attributs en attributs privés dans les classes Voiture et Proprietaire.

# Pour la classe Voiture:
# - marque -> lecture seule
# - modèle -> lecture seule
# - proprietaire -> lecture et écriture

# Pour la classe Proprietaire:
# - nom -> lecture seule
# - prenom -> lecture seule
# - date_naissance -> lecture seule

# Changer ce qu'il y a à changer dans les éléments de tests et programme principal.


from models import Proprietaire, Voiture
from datetime import date

# Création des propriétaires
proprietaire1: Proprietaire = Proprietaire("Geerts", "Quentin", date(1996, 4, 3))
# proprietaire1.nom = "Geerts"
# proprietaire1.prenom = "Quentin"
# proprietaire1.date_naissance = date(1996, 4, 3)

proprietaire2: Proprietaire = Proprietaire() # utilisation des valeurs par défaut
# proprietaire2.nom = "Adams"
# proprietaire2.prenom = "Michel"
# proprietaire2.date_naissance = date(1980, 1, 1)

print(proprietaire1)
print(proprietaire2.__str__())

# Création des voitures
voiture1: Voiture = Voiture("Kia", "Ceed", proprietaire1)
# voiture1.marque = "Kia"
# voiture1.modele = "Ceed"
# voiture1.proprietaire = proprietaire1

voiture2: Voiture = Voiture("Volkswaggen", "Polo", proprietaire2)
# voiture2.marque = "Volkswaggen"
# voiture2.modele = "Polo"
# voiture2.proprietaire = proprietaire2

print(voiture1)
print(voiture2)
