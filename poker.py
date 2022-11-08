import random
import numpy as np
from collections import Counter

# Array mit 52 Stellen erstellen 
# Jede Farbe hat 13 karten -> erste 13 Werte sind von der ersten Farbe usw. 
#   Der Wert % 13 gibt an welche karte bzw. welches Symbol ; Wert // 13 -> erlche der 4 Farben

# Regeln : https://www.cardschat.com/poker/strategy/poker-hands/royal-flush/
# https://i.pinimg.com/originals/ed/dd/01/eddd011194068c9971912d43d5c3ae06.jpg

rank = ['Royal Flush', 'Straight Flush', 'Four Of A Kind', 'Full House', 'Flush', 'Straight', 'Three Of A Kind','Two Pair', 'One Pair']
res = {}
for i in rank:
    res[i] =0

symb = [] #0-3
val = [] # 0-12 ; 12 ist das Ass


def get_cards():
    karten = np.arange(52)
    random.shuffle(karten)
    hand = karten[0:5]
    for i in range(len(hand)):
        symb.append(hand[i] // 13)
        val.append(hand[i] % 13)
  

# https://www.delftstack.com/de/howto/python/python-count-unique-values-in-list/

def multiples():
    return Counter(val).values()


def multiple_pairs():
    results  = list(multiples())
    return 2 in (Counter(results).values()) 


def flush():
    return (5 in  Counter(symb).values())


def straight():
    s = sorted(val)
    sum = 0
    for i in range(len(s)-1):
        if ((s[i] +1) == s[(i+1)]):
            sum += 1
    return sum == 4    


def update_dic():
    global val 
    val = []
    global symb
    symb = []
    
    get_cards()
   
    if flush() and straight() and (12 in val):
        res['Royal Flush'] +=1
    elif flush() and straight():
        res['Straight Flush'] +=1
    elif 4 in multiples():
        res['Four Of A Kind'] +=1
    elif (2 in multiples()) and (3 in multiples()):
        res['Full House'] +=1
    elif flush():
        res['Flush'] +=1
    elif straight():
        res['Straight'] +=1
    elif 3 in multiples():
        res['Three Of A Kind'] +=1
    elif multiple_pairs():
        res['Two Pair'] +=1
    elif 2 in multiples():
        res['One Pair'] +=1


def statistics(anz):
    for i in range(anz):
        update_dic()
    print(res)
    p = {}
    for i in rank:
        p[i] = (res[i] / anz) *100
    print(p)


statistics(100000)





