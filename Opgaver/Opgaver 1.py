#Anvend Pythons datastruktur list og dens metode sort til at
#Sortere en liste med 1000 tilfældigt genererede tal
import random

list = []

for i in range(1000):
    numbers = random.randint(1,100000)
    list.append(numbers)
print(list)

list.sort()

print(list)
