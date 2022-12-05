from enum import Enum

class abteilung(Enum):
    IT = 1
    Management = 2
    Vertrieb = 3
    Einkauf = 4

class person:
    def __init__(self, vname, nname,  alter, geschlecht):
        self.vname = vname
        self.nname = nname
        self.alter = alter 
        self.geschlecht = geschlecht

class mitarbeiter:
    pass

class gruppenLeiter:
    pass

def main():
    pass

if __name__ == "__main__":
    main()