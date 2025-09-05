try:
  from .proprietaire import Proprietaire
except:
  from proprietaire import Proprietaire
  
from datetime import date

# Déclaration de la classe
class Voiture:
  
  # Niveaux d'encapsulation:
  # - Public (symbole: )
  #     Accessible PARTOUT (dans la classe et en dehors)
  # - Protected (symbole: _) (pour l'héritage)
  #     Accessible uniquement dans la classe mère et ses filles (<!> sur papier)
  # - Private (symbole: __)
  #     Accessible UNIQUEMENT dans la classe
  
  # Attributs (caractéristiques)
  marque: str
  modele: str
  proprietaire: Proprietaire
  __cheveaux: int
  __couleur: str
  __turbo: bool
  
  # Constructeur
  def __init__(self, marque: str = "", modele: str = "", proprietaire: Proprietaire = None, cheveaux: int = 70, couleur: str = "Noir"):
    self.marque = marque
    self.modele = modele
    self.proprietaire = proprietaire
    self.cheveaux = cheveaux
    self.__couleur = couleur
    self.__turbo = False
    
    
  # Accesseurs et mutateurs (getters & setters)
  
  # Utilisation d'une annotation pour transformer la méthode en propriété
  @property
  def cheveaux (self):
    return self.__cheveaux

  @cheveaux.setter
  def cheveaux(self, valeur):
    if valeur < 0: raise ValueError("Les cheveaux doivent être strictement positif.")
    self.__cheveaux = valeur
    
  @property
  def details(self):
    return f"{self.marque} {self.modele}"
  
  # def __get_couleur (self): 
  #   return self.__couleur
  
  # def __set_couleur(self, value):
  #   self.__couleur = value
  
  
  
  # couleur = property(__get_couleur, __set_couleur)
  
  # Méthodes (comportements)
  def demarrer(self):
    print("La voiture démarre")
    self.__changer_mode()
    
  def arreter(self):
    print("La voiture s'arrête")
    self.__changer_mode()
      
  def rouler(self, distance: float):
    print(f"La voiture roule {distance} km")
    
  def __changer_mode(self):
    self.__turbo = not self.__turbo
    
  def __str__(self) -> str:
    return f"Marque: {self.marque}, modèle: {self.modele}" \
      + f", propriétaire: {self.proprietaire}"
  
if __name__ == "__main__":
  # Déclaration de la variable "voiture_test"
  # Instanciation: Création de l'objet en mémoire
  voiture_test: Voiture = Voiture("Kia", "Ceed", Proprietaire("Geerts", "Quentin", date(1996, 4, 3)))
  # voiture_test.marque = "Kia"
  # voiture_test.modele = "Ceed"
  voiture_test.cheveaux = 110
  print(f"Cheveaux: {voiture_test.cheveaux}")
  
  print(f"Détails: {voiture_test.details}")
  # print(f"Couleur: {voiture_test.couleur}")
  # print(f"Couleur: {voiture_test.__get_couleur()}")
  
  print(f"Couleur privée: {voiture_test._Voiture__couleur}")
  
  # voiture_test.__changer_mode()
  
  
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