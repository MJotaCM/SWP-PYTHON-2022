import random
import numpy as np

#Aufgabe Programmiere Lottoziehung als Methode:
#Aufgabe 1 
def zahlen_ziehen(start, end, anz):
    all = np.arange(start, end+1)
    random.shuffle(all)
    return all[0:anz]

# Swap-Funktion
# list[0] , list[1] = list[1], list[0]

#Aufgabe 2
def statistik(start, end, anz):
    d = dict.fromkeys(np.arange(start, end+1), 0)
    for i in range(anz):
        d[int(random.random()*end + 1)] += 1
    return d

print(zahlen_ziehen(1,45,6))
print(statistik(1,45,1000))