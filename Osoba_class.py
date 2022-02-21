from pickle import FALSE


class Osoba:
    def __init__(self, adresa, zamestani, jmeno, prijmeni, vek): # toto je constructor
        self.adresa = adresa
        self.zamestnani = zamestani
        self.cele_jmeno = jmeno + " " + prijmeni
        self.vek = vek
    
    def je_duchodce(self):
        if self.vek > 65:
            return True
        else:
            return False
    
    def pozdrav(self): # self parametr, který obsahuje instanci
        print 

        
nicol = Osoba("Praha", "OSVC", "Nicol", "Gotzova", 28)
print (nicol.cele_jmeno)
tomas = Osoba("Praha", "Avast", "Tomas", "Daněk", 96)
print (tomas.zamestnani, tomas.adresa)
print (nicol.je_duchodce() ,tomas.je_duchodce())

