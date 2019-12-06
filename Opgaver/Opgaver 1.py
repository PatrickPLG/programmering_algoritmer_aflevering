#Anvend Pythons datastruktur list og dens metode sort til at
#Sortere en liste med 1000 tilfældigt genererede tal
import random


numbers = random.randint(0,1000)

numbersList = list(numbers)
numbersList.sort()

print(numbersList)
