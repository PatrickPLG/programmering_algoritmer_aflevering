# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000

#Der bruges 10000 forskellige tal, siden 100.000 osv. vil tage for lang tid.

import time
import random

numGen = 10000
times = []

def randomSort(A):
    number = A
    number.sort()
    print(len(number))
    return number

for i in range(4):
    StartT = "start" + str(i)
    StopT = "slut" + str(i)
    StartT = time.time()
    talliste = random.sample(range(1000000), numGen)
    
    print(randomSort(talliste))
    StopT = time.time()
    numGen = numGen + 10000
    trueTime = StopT-StartT
    times.append(trueTime)
    
print("")
print(times)
print("Sammenlagt tid")
print(sum(times))