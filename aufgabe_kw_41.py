import random
import numpy as np

# Array mit 52 Stellen erstellen 
# Jede Farbe hat 13 karten -> erste 13 Werte sind von der ersten Farbe usw. 
#   Der Wert % 13 gibt an welche karte bzw. welches Symbol ; Wert // 13 -> erlche der 4 Farben

karten = np.arange(52)
random.shuffle(karten)
hand =  karten[0:5]
print(hand)

def cards_are_same():
    pass
