import random
import numpy as np

#Aufgabe Programmiere Lottoziehung als Methode:
#Aufgabe 1 
all = np.arange(1, 46)
random.shuffle(all)
print(all[0:6])

#Aufgabe 2
md = dict.fromkeys(np.arange(1, 46), 0)
for i in range(0, 1000):
    md[int(random.random()*45 + 1)] += 1
print(md)
