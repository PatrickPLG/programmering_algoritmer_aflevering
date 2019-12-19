# Brug Modulet 'time' til at tage tid på kørsleb af 'sort'
# for fire forskellige størrelser input.
# For eksempel 100.000, 200.000, 300.000 og 400.000

# Importerer modulerne time og randome
import time
import random

# Laver en variabel ved navn numGen og et array der hidder times
numGen = 100000
times = []


def randomSort(A):
    # sætter number til at være funktionen randomSort
    number = A
    # Sorterer number
    number.sort()
    # Printer længden a number arrayet
    print(len(number))
    # Returnerer number arrayet
    return number


chooseAmount = input("Vil du selv bestemme hvor mange tal der skal sorteres\
 eller skal der køres standard mængde? selv/standard ")

# Starter en forgrening ud fra chooseAmount inputtet
if (chooseAmount == "standard"):
    # Hvis der er skrevet "standard"
    # går den i gang med at sorterer 100.000, 200.000, 300.000 og 400.000 tal
    for i in range(4):
        # Først sættes StartT variablen til at være
        # programmets daværende uptime
        StartT = time.time()
        # Så udvælger den mængden af tal angivet i numGen variablen
        # i en liste fra 0-1.000.000
        # og sætter disse tal til at være i arrayet talliste
        talliste = random.sample(range(1000000), numGen)
        # Så printer den tallisten,
        # hvor den er kørt igennem funktionen randomSort
        print(randomSort(talliste))
        # Så laver den variablen StopT som er programmets uptime
        StopT = time.time()
        # Variablen numGen forhøjes med 100.000
        numGen = numGen + 100000
        # Variablen trueTime bliver nu lavet og sat til at være StopT-StartT
        trueTime = StopT-StartT
        # Variablen trueTime bliver nu sat ind i arrayet times
        times.append(trueTime)
elif (chooseAmount == "selv"):
    # Der laves en heltals variabel ved navn amount
    amount = int(input("Hvor mange tal skal sorteres? "))
    # Sætter StartT til programmets daværende uptime
    StartT = time.time()
    # Så udvælger den mængden af tal angivet i amount variablen
    # i en liste af tal med størrelsen amount * 100
    talliste = random.sample(range(amount * 100), amount)
    # Så printer den tallisten, hvor den er kørt igennem funktionen randomSort
    print(randomSort(talliste))
    # Så laver den variablen StopT som er programmets uptime
    StopT = time.time()
    # Variablen trueTime bliver nu lavet og sat til at være StopT-StartT
    trueTime = StopT-StartT
    # Variablen trueTime bliver nu sat ind i arrayet times
    times.append(trueTime)

# Printer både arrayet times og summen af times
print("")
print(times)
print("Sammenlagt tid")
print(sum(times))
