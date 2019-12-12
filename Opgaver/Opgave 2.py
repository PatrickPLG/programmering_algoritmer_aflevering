# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000
import time
import random

def randomSort(A):
    tal = A
    tal.sort()
    print(len(tal))
    return tal

for i in range(4):
    "start" + str(i)



start1 = time.time()
talliste = random.sample(range(1000000), 10000)
print(talliste)
print(randomSort(talliste))
slut1 = time.time()


start2 = time.time()
talliste = random.sample(range(1000000), 20000)
print(talliste)
print(randomSort(talliste))
slut2 = time.time()


start3 = time.time()
talliste = random.sample(range(1000000), 30000)
print(talliste)
print(randomSort(talliste))
slut3 = time.time()


start4 = time.time()
talliste = random.sample(range(1000000), 40000)
print(talliste)
print(randomSort(talliste))
slut4 = time.time()


print("")
print("Resultaterne er:")
print("1000" + slut1 - start1)
print("2000" + slut2 - start2)
print("3000" + slut3 - start3)
print("4000" + slut4 - start4)
print("Gennemsnitettet er:")
slutG = (slut1+slut2+slut3+slut4)/4
startG = (start1+start2+start3+start4)/4
print(slutG-startG)