# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000

#Der bruges 10000 forskellige tal, siden 100.000 osv. vil tage for lang tid.

import time
import random

numGen = 10000
tider = []

def randomSort(A):
    tal = A
    tal.sort()
    print(len(tal))
    return tal

for i in range(4):
    test = "start" + str(i)
    test2 = "slut" + str(i)
    test = time.time()
    talliste = random.sample(range(1000000), numGen)
    
    print(randomSort(talliste))
    test2 = time.time()
    numGen = numGen + 10000
    tidS = test2-test
    tider.append(tidS)
    
print("")
print(tider)
print("Sammenlagt tid")
print(sum(tider))