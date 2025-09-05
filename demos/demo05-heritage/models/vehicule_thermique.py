from .vehicule import Vehicule

class VehiculeThermique (Vehicule):
  
  __capacite_carburant: int
  
  def __init__(self, marque: str, modele: str, annee_fabrication: int, capacite_carburant: int):
    # self.__marque = marque
    # self.__modele = modele
    # self.__annee_fabrication = annee_fabrication
    # super().__init__(marque, modele, annee_fabrication)
    Vehicule.__init__(self, marque, modele, annee_fabrication)
    self.__capacite_carburant = capacite_carburant
    
  @property
  def capacite_carburant(self) -> int:
    return self.__capacite_carburant
  
  def demarrer(self) -> None:
    print(f"Le vehicule thermique démarre")
  
  
  def __str__ (self) -> str:
    return f"{super().__str__()} avec {self.capacite_carburant}L de carburant"
