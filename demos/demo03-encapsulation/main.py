# Exercice 02

# Reprenez la démonstration 02 (demo02-constructeurs).
# Créer un constructeur pour la classe Voiture qui permettra d'initialiser les différents champs.
# Changer également les lignes dans la partie des tests et du programme principal pour que le code continue de fonctionner.


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
