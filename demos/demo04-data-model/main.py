from models import Proprietaire, Voiture
from datetime import date

# Création des propriétaires
proprietaire1: Proprietaire = Proprietaire("Geerts", "Quentin", date(1996, 4, 3))

print(proprietaire1)

# Création des voitures
voiture1: Voiture = Voiture("Kia", "Ceed", proprietaire1, 110, "Rouge", numero_chassis="123456789")
voiture2: Voiture = Voiture("Kia", "Ceed", proprietaire1, 110, "Rouge", numero_chassis="123456789")

print(voiture1)


print(Proprietaire.__name__ == "Proprietaire") # True
print(f"Proprietaire.__bases__: {Proprietaire.__bases__}") # (<class 'object'>,)
print(f"proprietaire1.__class__: {proprietaire1.__class__}") # <class 'models.proprietaire.Proprietaire'>

print(f"Dict de voiture1: {voiture1.__dict__}") # {'_Voiture__marque': 'Kia', '_Voiture__modele': 'Ceed', '_Voiture__proprietaire': <models.proprietaire.Proprietaire object at 0x00000256AC12FE00>, '_Voiture__cheveaux': 70, '_Voiture__couleur': 'Noir', '_Voiture__turbo': False}
print(f"Doc de Voiture: {Voiture.__doc__}")
# print(f"Doc de la méthode: {_Voiture_marque.__doc__}")

print(f"__repr__: {voiture1.__repr__()}")


print(f"voiture1 == voiture2: {voiture1 == voiture2}") # True
print(f"voiture1 != voiture2: {voiture1 != voiture2}") # False

