# Pytonversion vor oder nach 3.7?
# pdp p...print

#Ternary Operator in Python
#Andere Schreibweise f¸r if
# a=5
# val = True if a > 5 else False

#Mapper
#   iterierbare listen: list, tuple (2 Methoden(iter, next))
#   map object ist auch iterierbar

#Lambda
#   Methode existiert nur an dieser Stelle, anonyme Funktion

#OO
#   private, protected usw. gibt es in Python nicht
#   - G¸ltigkeitsbereich mˆglichst klein -> Kapselung (Struktur entsteht)
#       Seiteneffekte auch bei Kapselung
#       Wenn man eine Variable global macht kann man von der auﬂeren zugreifen

#   __init__ = Kontruktor
#   self = this
#   static...gehˆrt zu der Klasse / Klassenattribut (das anderes der Instanz) Instanzvariablen
#       satic variablen auﬂerhalb der Methode aber in der Klasse -> Static
#   Klassen Objekte sind mutable
#   Vererbung weil erweiterbar
#   Struktur der Elternklasse an Kindklasse ¸bergeben  
#   super ... tempor‰re Instanz von Elternklasse erzeugt auf die man dann zugreifen kann
#             super ist eine Referenz 
#   Java interfaces -> mehrfachvereerbung

#   super(square, self) geht auf die Ebene Square und auf die Elternklasse
#       Java: super.super.super
#   Mehrfachvererbung Reihenfolge wichtig (wenn in beiden Klassen gleichnamige Methode -> nimmt die von der ersten)
#   __mro__ -> Reihenfolge der Vererbung anschauen

#   Bitmuster
#   Computerlogik 
#   Flask api  | api struktur dokumentieren

#Virtual Environment
#   Sind an Betriebssystem und Umgebung gekoppelt

#   Spezielle Programmierumgebung haben z.B f¸r eine Library braucht man ne andere Version
#   Python rohinstallation wird in einem Ordenr auf der Festplatte erweitert. Die Bibliotheken, die man runterladet bleiben  auch nur in dem Ordner
#   2 Befehle: pip (install)
#   requirement.txt -> pip freeze > in datei rein pipen ;  pip install -r requirement.txt
#       pip install pipreqs (pip freeze alle imports werden reingeschrieben; pip reqs schaut nach was im Programm wirklich verwendet wird und importiert das)
#           wenns nicht funktioniert pip install wheel

#   py -m venv venv(Ordner)
#       -> bin-Ordner: Referenz auf Python vom System
#   source venv/bin/activate : aktiviert des environment
#   deactivat : man ist wieder aus dem virtual environment drauﬂen

# System exakt nachbilden