import random

# laver en varibel numGen og sætter den til 1000
numGen = 1000


def selection_sort(A):
    # Der oprettes et array af tal ved navn tallist
    # og en variabel n som er længden af tallist
    tallist = A
    n = len(tallist)

    # Der oprettes en løkke i som er længden af tallisten -1
    for i in range(n-1):
        # mini variablen sættes til at være i
        mini = i

        # Der oprettes en løkke j
        # som længden mellem variablen i +1 til længden af n
        for j in range(i + 1, n):
            # Hvis tallist[j] er mindre en tallist[mini]
            # sættes mini til at være j
            if tallist[j] < tallist[mini]:
                mini = j
        # Hvis mini ikke er lig med i
        # bytter den om på tallist[mini] og tallist[i]
        if mini != i:
            tallist[mini], tallist[i] = tallist[i], tallist[mini]
    # Resultatet af den sorterede tallist skrives i terminalen
    return tallist


chooseAmount = input("Vil du selv bestemme hvor mange tal der skal sorteres\
 eller skal der køres standard mængde? selv/standard ")

# Starter en forgrening ud fra chooseAmount inputtet
if (chooseAmount == "standard"):
    # Hvis der er skrevet "standard"
    # går den i gang med at sorterer 100.000, 200.000, 300.000 og 400.000 tal
    for s in range(4):
        # Så udvælger den mængden af tal angivet i numGen variablen
        # i en liste fra 0-1.000.000
        # og sætter disse tal til at være i arrayet talliste
        talliste = random.sample(range(1000000), numGen)
        # Så printer den tallisten,
        # hvor den er kørt igennem funktionen selection_sort
        print(selection_sort(talliste))
        # Variablen numGen forhøjes med 100.000
        numGen = numGen + 1000
        # Variablen trueTime bliver nu lavet og sat til at være StopT-StartT
elif (chooseAmount == "selv"):
    # Der laves en heltals variabel ved navn amount
    amount = int(input("Hvor mange tal skal sorteres? "))
    # Så udvælger den mængden af tal angivet i amount variablen
    # i en liste af tal med størrelsen amount * 100
    talliste = random.sample(range(amount * 100), amount)
    # Så printer den tallisten,
    # hvor den er kørt igennem funktionen selection_sort
    print(selection_sort(talliste))
