# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000

#Der bruges 10000 forskellige tal, siden 100.000 osv. vil tage for lang tid.

import time
import random

numGen = 100000
times = []

def randomSort(A):
    number = A
    number.sort()
    print(len(number))
    return number

chooseAmount = input("Vil du selv bestemme hvor mange tal der skal sorteres\
 eller skal der køres standard mængde? selv/standard ")
if (chooseAmount == "standard"):
    for i in range(4):
        StartT = time.time()
        talliste = random.sample(range(1000000), numGen)
        print(randomSort(talliste))
        StopT = time.time()
        numGen = numGen + 100000
        trueTime = StopT-StartT
        times.append(trueTime)
elif (chooseAmount == "selv"):
    amount = int(input("Hvor mange tal skal sorteres? "))
    StartT = time.time()
    talliste = random.sample(range(amount + 1), amount)
    print(randomSort(talliste))
    StopT = time.time()
    trueTime = StopT-StartT
    times.append(trueTime)
    
print("")
print(times)
print("Sammenlagt tid")
print(sum(times))