# kw_41 ; 12.10.2022

# tuple und liste Unterschied: tuple ist eine final-liste
# tuple ist eine Liste, die nicht mehr ver�ndert werden kann
# dictionary ist unsortiert
#   mtuple = (1,2)
#   type(mtuple)

# Shebang:
#   #!/usr/bin/env python3
#   Sagt wer der Interpreter ist
#   # .... Kommentar , ! , Bash

# Pass-Anweisung:
#   def meine_funktion():
#       pass
#   meine_funktion()
# pass wird verwendet als Platzhalter, damit kein Fehler kommt, wenn man die Methode noch nicht ausprogrammiert hat; wird �bersprungen

# Division:
#   a = 6, b = 5 , a/b = 1.2
#   Python 2 gleich wie in Java w�rde man nur 1 bekommen
#   Um die gleiche Funktionalit�t zu bekommen: a // b = 1 ... Floor Division (Man k�nnte auch a/b Typcasten, sollte man aber nicht machen)

# Auswertungsreihenfolge der Operatoren:
#   Lamdafunktion -> Anonyme Funktion
#       ...schneller , weil im Stack keine Speicher extra f�r die Funktion angelegt wird

# Referenz, Instanz , Identit�t:
#   Instanz: wenn man ein neues Objekt einer Klasse macht / C++ ... Structure
#   Referenz: C++ ... Pointer / Java ... Symbolische Link / Python ... Referenz
#   Identit�t: ... Fingerabdruck von einem Objekt
#       zahl = 8 (Instanz ... 8 ; Referenz .... zahl = )
#       id(zahl) ... Identit�t von der Speicherstelle wo der 8er liegt  == id(8) ... weil der 8er nur ein Mal gespeichert wird
# (immutable ...  (int) wird nur einmal ins Speicher rein gelegt, id kann gleich sein)
# (mutable ... primitive Datentypen (Listen, Arrays, usw.) -> haben immer andere ids auch wenn 2 Listen gleich sind)
# https://openbook.rheinwerk-verlag.de/python/07_001.html ...  fragt das n�chstes Mal
# v1 == v2 ... Inhalt wird verglichen (in Java nicht ... equals)

# Garbage Collector:
#   Referenzz�hler wird angelegt wenn man den Speicher anlegt
#   a = 5 -> Referenzz�hler wird um 1 erh�ht ; b = a -> Referenzz�hler = 2
#   Garbagecollector schaut ob der Referenzz�hler 0 ist -> wenn ja, er gibt die Stelle frei zum �berchreiben

# Instanzen freigeben mit del
#   del Referenz -> Garbage Collector wei� er soll die Speicherstelle freigeben (Soll man in Java, Python, C# eigentlich nicht machen)

# mutable ; immutable
#   list, bytearray ... sequenzielle Datentypen 
#   liste ... ver�nderlich -> Mutable (Mutable haben Seiteneffekte)
#       l1 = [1,2] ; l2 = l1 ; l1.append(3) -> l1 sowie l2 sind jetzt [1,2,3] weil mehrere Referenzen auf die gleiche Instanz zeigen
#            -> Damit das nicht passiert - Deep Copy
#   tuple, int, float ... unver�nderlich -> Immutable

# Haus�bung : 
# Wie werden Parameter einer Methode �bergeben: (mutable , global oder lokal ver�ndert)
# + Poker (soll in 3 Wochen fertig sein)
