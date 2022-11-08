# Pyton ist einee Interpretersprache
# C++ wird direkt zu Maschienencode
# interpreter macht den Maschienencode zu einem Bytecode
# Java, Python, C# compelieren den Code zu Bytecode und nicht Maschienencode

# Maschinencode kann nur auf der spezifischen Maschiene ausführen -> gebunden da nur für ein bestimmten Typen von CPUs (C)
#   ist aber m schnellsten für diese Hardware

# Interpreter: (python: pyc,java: class-Datei)
#   Vorteile: sind immmer Plattformunabhängig
#   Class datei wird durch den Interpreter noch mal nachkompiliert
#   Nachteil: vieles wird von der Sprache selbst verwaltet z.B Speicher
#             nicht 100% effizient -> langsamer

# Java , Pyton , C# -> C -> Assembler (Binärzeichen; 3 Buchtabige Befehle)

# Mutable;immutable
#   in-place:  wenn wir einen von n Elemente abhängigen Speicher brauchen bei Operationen
#   Liste Sortierten: neue Liste braucht man 
#   List2 = sortieren Liste1 .... in-place

# Copy - DeepCopy
# Liste mit immutable objekte -> copy 
# DeepCopy: alles wird kopiert (alle Objeke) nicht nur referenzen
# Copy: nur die Referenz wird kopiert

# Wenn man eine Zeile auf 2 aufteilen will -> bei der ersten Zeile einen Backslash hinzufügen

# Encoding (UTF-8)

#HackerRank
# Dunder-Variablen
#   variablen die (in dem Einstigspunkt) in der Main
#   if __name__ = "__main__":
#       meine_funktion()
#   __variable ... Dunder-Variablen; pro File eine
#   __name__ ... das Programm bekommt den eigenen Namen z.B Test.py ; die datei die man mit dem Interpreter gestartet hat -> bekommt __main__ zurück
