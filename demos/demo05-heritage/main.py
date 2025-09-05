from models import Vehicule, VehiculeThermique, VehiculeElectrique, VehiculeHybride


vehicule1: Vehicule = Vehicule("Kia", "Ceed", 2019)

vehiculeT1: VehiculeThermique = VehiculeThermique("Kia", "Ceed", 2019, 40)
vehiculeE1: VehiculeElectrique = VehiculeElectrique("Renault", "Zoé", 2022, 300)

print(vehicule1)
print(vehiculeT1)
print(vehiculeE1)

vehiculeT1.demarrer()
vehiculeT1.rouler(800)
vehiculeT1.arreter()

vehiculeE1.demarrer()
vehiculeE1.rouler(100)
vehiculeE1.arreter()

vehiculeH1: VehiculeHybride = VehiculeHybride("Toyota", "Yaris", 2025, 30, 700)
vehiculeH1.demarrer() # MRO: Method Resolution Order


print(vehiculeH1)