from .vehicule import Vehicule

class VehiculeElectrique (Vehicule):
  
  __autonomie: int
  
  def __init__(self, marque: str, modele: str, annee_fabrication: int, autonomie: int):
    # super().__init__(marque, modele, annee_fabrication)
    Vehicule.__init__(self, marque, modele, annee_fabrication)
    self.__autonomie = autonomie
    
  @property
  def autonomie(self) -> int:
    return self.__autonomie
  
  def demarrer(self) -> None:
    print(f"Le vehicule electrique démarre")
  
  def __str__(self) -> str:
    return f"{super().__str__()} avec une autonomie de {self.autonomie} km"