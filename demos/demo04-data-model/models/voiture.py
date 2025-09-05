try:
  from .proprietaire import Proprietaire
except:
  from proprietaire import Proprietaire
  
from datetime import date

# Déclaration de la classe
class Voiture:
  """La classe représentant une voiture

  Raises:
      ValueError: _description_
      ValueError: _description_
  """
  # Attributs (caractéristiques)
  __marque: str
  __modele: str
  __proprietaire: Proprietaire
  __cheveaux: int
  __couleur: str
  __turbo: bool
  __numero_chassis: str
  
  # Constructeur
  def __init__(self, marque: str = "", modele: str = "", proprietaire: Proprietaire = None, cheveaux: int = 70, couleur: str = "Noir", numero_chassis: str = ""):
    self.__marque = marque
    self.__modele = modele
    self.proprietaire = proprietaire
    self.cheveaux = cheveaux
    self.__couleur = couleur
    self.__numero_chassis = numero_chassis
    self.__turbo = False
    
    
  # Accesseurs et mutateurs (getters & setters)
  
  # Utilisation d'une annotation pour transformer la méthode en propriété
  @property
  def marque(self) -> str:
    """Propriété de la marque

    Returns:
        str: La marque de la voiture
    """
    return self.__marque
  
  @property
  def modele(self):
    return self.__modele
  
  @property
  def proprietaire(self):
    return self.__proprietaire
  
  @proprietaire.setter
  def proprietaire(self, value):
    if value is not None and not isinstance(value, Proprietaire): 
      raise ValueError("Le propriétaire doit être de la classe Propriétaire")
    self.__proprietaire = value
  
  @property
  def cheveaux (self):
    return self.__cheveaux

  @cheveaux.setter
  def cheveaux(self, valeur):
    if valeur < 0: raise ValueError("Les cheveaux doivent être strictement positif.")
    self.__cheveaux = valeur
    
  @property
  def numero_chassis(self) -> str:
    return self.__numero_chassis
    
  @property
  def details(self):
    return f"{self.marque} {self.modele}"
  
  # Méthodes (comportements)
  def demarrer(self):
    """Méthode permettant le démarre de la voiture.
    """
    print("La voiture démarre")
    self.__changer_mode()
    
  def arreter(self):
    print("La voiture s'arrête")
    self.__changer_mode()
      
  def rouler(self, distance: float):
    """Méthode permettant de rouler une certaine distance.

    Args:
        distance (float): La distance à parcourir.
    """
    print(f"La voiture roule {distance} km")
    
  def __changer_mode(self):
    self.__turbo = not self.__turbo
    
  
  # Redéfinition des méthodes magiques
  def __repr__(self) -> str: # représentation officielle
    return f"Voiture[marque={self.marque},modele={self.modele},proprietaire={self.proprietaire}]"
  
  def __str__(self) -> str: # représention informelle
    return f"Marque: {self.marque}, modèle: {self.modele}" \
      + f", propriétaire: {self.proprietaire}"
      
  # Redéfinition des méthodes magiques de comparaison
  def __eq__(self, o: object) -> bool:
    if not isinstance(o, Voiture): return False
    return self.numero_chassis == o.numero_chassis
  
  # Si vous définissez le comportement d'un opérateur de comparaison
  # vous devez également redéfinir son complémentaire
  def __ne__(self, o: object) -> bool:
    return not (self.numero_chassis == o.numero_chassis)
  
if __name__ == "__main__":
  # Déclaration de la variable "voiture_test"
  # Instanciation: Création de l'objet en mémoire
  voiture_test: Voiture = Voiture("Kia", "Ceed", Proprietaire("Geerts", "Quentin", date(1996, 4, 3)))
  voiture_test.cheveaux = 110
  print(f"Cheveaux: {voiture_test.cheveaux}")
  
  print(f"Détails: {voiture_test.details}")
  print(f"Couleur: {voiture_test.couleur}")
  
  voiture_test.demarrer()
  voiture_test.rouler(50)
  voiture_test.arreter()
  
  print(f"Voiture: {voiture_test}")
  print(f"Propriétaire: {voiture_test.proprietaire}")