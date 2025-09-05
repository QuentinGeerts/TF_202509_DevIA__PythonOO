
class Vehicule:
  # Attributs
  __marque: str
  __modele: str
  __annee_fabrication: int
  
  
  # Constructeurs
  def __init__(self, marque: str, modele: str, annee_fabrication: int):
    self.__marque = marque
    self.__modele = modele
    self.__annee_fabrication = annee_fabrication
    
    
  # Getters
  @property
  def marque(self) -> str:
    return self.__marque
  
  @property
  def modele(self) -> str:
    return self.__modele
  
  @property
  def annee_fabrication(self) -> int:
    return self.__annee_fabrication
  

  # Méthodes (comportements)
  def demarrer(self):
    print("La vehicule démarre")
    
  def arreter(self):
    print("La vehicule s'arrête")
      
  def rouler(self, distance: float):
    print(f"La vehicule roule {distance} km")

  
  def __str__(self) -> str:
    return f"{self.marque} {self.modele} de {self.annee_fabrication}"  
