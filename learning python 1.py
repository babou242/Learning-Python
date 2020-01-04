# Silmulateur de vile
# création de la classe batiment
class Batiment:
    def __init__ (self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages
    
    def get_adresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages 

class Immeuble(Batiment):
    def __init__(self, adresse, nb_etages, nb_balcon):
        super().__init__(adresse, nb_etages)
        self.nb_balcon = nb_balcon
class Supermarche(Batiment):
    def __init__(self, adresse, nb_etages, nb_rayon):
        super().__init__(adresse, nb_etages)
        self.nb_rayon = nb_rayon
class Banque(Batiment):
    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        super().__init__(adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom

flandre = Immeuble("49 rue de chatenay , Antony", 12, 96)
daufine = Immeuble("25 rue de Verdun , Fresnes", 6 , 48)

print(flandre.get_adresse())