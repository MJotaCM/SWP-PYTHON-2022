from enum import Enum

class Abteilung(Enum):
    IT = 0
    Management = 1
    Vertrieb = 2
    Einkauf = 3


class Geschlecht(Enum):
    m = 0
    w = 1 
    d = 2
      

class Person:
    def __init__(self, vname, nname, geschlecht: Geschlecht):
        self.vname = vname
        self.nname = nname
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, vname, nname, geschlecht: Geschlecht, abteilung: Abteilung):
        super().__init__(vname, nname, geschlecht)
        self.abteilung = abteilung
       

class GruppenLeiter(Mitarbeiter):
    def __init__(self, vname, nname, geschlecht: Geschlecht, abteilung: Abteilung, gruppe: int):
        super().__init__(vname, nname, geschlecht, abteilung)
        self.gruppe = gruppe
       

class Firma:
    def __init__(self, mitarbeiter = None, name = 'Audi'):
        self.mitarbeiter = [] if mitarbeiter is None else mitarbeiter
        self.name = name
        
    def einige_mitarbeiter_erstellen(self):
        self.mitarbeiter.append(Mitarbeiter('Toni','Mayr', Geschlecht.m, Abteilung.IT))
        self.mitarbeiter.append(Mitarbeiter('Emma','Huber', Geschlecht.w, Abteilung.Vertrieb))
        self.mitarbeiter.append(GruppenLeiter('Herbert','Maier', Geschlecht.m, Abteilung.Management, 13))
        self.mitarbeiter.append(GruppenLeiter('Herbert','Maier', Geschlecht.m, Abteilung.Management, 13))

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)

    def anzahl_leiter(self):
        c = 0
        for i in self.mitarbeiter:
            if type(i) == GruppenLeiter: c += 1  
        return c

    def anzahl_abteilungen(self):
        abt = []
        for i in self.mitarbeiter:
            if not i.abteilung in abt: abt.append(i.abteilung) 
        return len(abt)

    # noch zu machen
    def groesste_abteilung(self):
        abt = {}
        for i in self.mitarbeiter:
            if i.abteilung.name in abt.keys():
                abt[i.abteilung.name] += 1
            else:
                abt[i.abteilung.name] = 1
        department = list(abt.keys())[0]
        for d in abt.keys():
            if abt[department] < abt[d]:
                department = d
        return department


    def w_m_verhaeltnis(self):
        d = {'m': 0, 'w':0, 'd': 0}
        for i in self.mitarbeiter:
            d[i.geschlecht.name] += 1
         
        for k in d.keys():
            d[k] = round(d[k] / len(self.mitarbeiter), 3)
        return d


def main():
    f1 = Firma()
    f1.einige_mitarbeiter_erstellen()
    print(f1.anzahl_abteilungen())
    print(f1.anzahl_leiter())
    print(f1.anzahl_mitarbeiter())
    print(f1.w_m_verhaeltnis())
    print(f1.groesste_abteilung())


if __name__ == "__main__":
    main()