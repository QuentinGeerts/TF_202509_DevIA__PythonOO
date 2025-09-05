try:
  from .proprietaire import Proprietaire
except:
  from proprietaire import Proprietaire
  
from datetime import date

# Déclaration de la classe
class Voiture:
  
  # Attributs (caractéristiques)
  marque: str
  modele: str
  proprietaire: Proprietaire
  
  # Constructeur
  def __init__(self, marque: str = "", modele: str = "", proprietaire: Proprietaire = None):
    self.marque = marque
    self.modele = modele
    self.proprietaire = proprietaire
  
  # Méthodes (comportements)
  def demarrer(self):
    print("La voiture démarre")
    
  def arreter(self):
    print("La voiture s'arrête")
      
  def rouler(self, distance: float):
    print(f"La voiture roule {distance} km")
    
  def __str__(self) -> str:
    return f"Marque: {self.marque}, modèle: {self.modele}" \
      + f", propriétaire: {self.proprietaire}"
  
if __name__ == "__main__":
  # Déclaration de la variable "voiture_test"
  # Instanciation: Création de l'objet en mémoire
  voiture_test: Voiture = Voiture("Kia", "Ceed", Proprietaire("Geerts", "Quentin", date(1996, 4, 3)))
  # voiture_test.marque = "Kia"
  # voiture_test.modele = "Ceed"
  
  # proprietaire_test: Proprietaire = Proprietaire()
  # proprietaire_test.nom = "Geerts"
  # proprietaire_test.prenom = "Quentin"
  # proprietaire_test.date_naissance = date(1996, 4, 3)
  
  # voiture_test.proprietaire = Proprietaire("Geerts", "Quentin", date(1996, 4, 3))
  
  voiture_test.demarrer()
  voiture_test.rouler(50)
  voiture_test.arreter()
  
  print(f"Voiture: {voiture_test}")
  print(f"Propriétaire: {voiture_test.proprietaire}")
  print(f"Nom du Propriétaire: {voiture_test.proprietaire.nom}")