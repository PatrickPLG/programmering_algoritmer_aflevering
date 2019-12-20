# Anvend Pythons datastruktur list og dens metode sort til at
# Sortere en liste med 1000 tilfældigt genererede tal

import random

# opretter en liste uden indhold
list = []

# kører igennem løkken 1000 gange
for i in range(1000):
    # sætter numbers til random numre mellem 1 og 100000
    numbers = random.randint(1, 100000)
    # ligge numrene der er lige genereret ind i list
    list.append(numbers)

# Printer den usorteret liste
print("Liste - Ikke sorteret")
print(list)

# sortere listen og herefter bliver den printet
list.sort()
print("Liste - Sorteret")
print(list)
