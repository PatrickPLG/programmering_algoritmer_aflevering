# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000
import time
import random

def randomSort(A):
    tal = random.sample(range(1000000), A)
    tal.sort()
    print(len(tal))
    return tal


numGen = 100000
print(randomSort(numGen))
