from .vehicule_thermique import VehiculeThermique
from .vehicule_electrique import VehiculeElectrique
from .vehicule import Vehicule

class VehiculeHybride(VehiculeThermique, VehiculeElectrique):
  
  def __init__(self, marque: str, modele: str, annee_fabrication: int, capacite_carburant: int, autonomie: int):
    VehiculeThermique.__init__(self, marque, modele, annee_fabrication, capacite_carburant) # Manuel
    VehiculeElectrique.__init__(self, marque, modele, annee_fabrication, autonomie) # Manuel
    
  
  def __str__(self) -> str:
    return f"{Vehicule.__str__(self)}"