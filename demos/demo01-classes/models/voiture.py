# Déclaration de la classe
class Voiture:
  
  # Attributs (caractéristiques)
  marque: str
  modele: str
  
  # Méthodes (comportements)
  def demarrer(self):
    print("La voiture démarre")
    
  def arreter(self):
    print("La voiture s'arrête")
      
  def rouler(self, distance: float):
    print(f"La voiture roule {distance} km")
  
if __name__ == "__main__":
  # Déclaration de la variable "voiture_test"
  # Instanciation: Création de l'objet en mémoire
  voiture_test: Voiture = Voiture()
  voiture_test.marque = "Kia"
  voiture_test.modele = "Ceed"
  voiture_test.demarrer()
  voiture_test.rouler(50)
  voiture_test.arreter()
  
  print(f"Voiture: {voiture_test}" \
        + f"\n - Marque: {voiture_test.marque}" \
        + f"\n - Modèle: {voiture_test.modele}")