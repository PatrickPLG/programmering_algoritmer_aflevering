# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000
import time
start = time.time()

import random

numGen = 100000

def randomNumber(A):
    for i in range(numGen):
        numbers = random.sample(range(numGen), numGen)
    A.append(numbers)
    A.sort()
print(randomNumber(100000))