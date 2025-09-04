from datetime import date

class Proprietaire:
  nom: str
  prenom: str
  date_naissance: date
  
  # Redéfinition de méthodes (POO: Héritage)
  def __str__(self) -> str:
    return f"{self.nom} {self.prenom} né le {self.date_naissance.strftime("%d/%m/%Y")}"
  
if __name__ == "__main__":
  proprio: Proprietaire = Proprietaire()
  proprio.nom = "Geerts"
  proprio.prenom = "Quentin"
  proprio.date_naissance = date(1996, 4, 3)
  print(f"Propriétaire: {proprio}")