import random

numGen = 1000

def selection_sort(A):
    tallist = A
    n = len(tallist)

    for i in range(n-1):
        mini = i
        
        for j in range(i+1,n):
            if tallist[j] < tallist[mini]:
                mini = j
        if mini != i:
            tallist[mini],tallist[i] = tallist[i], tallist[mini]
    return tallist

chooseAmount = input("Vil du selv bestemme hvor mange tal der skal sorteres\
 eller skal der køres standard mængde? selv/standard ")

# Starter en forgrening ud fra chooseAmount inputtet 
if (chooseAmount == "standard"):
    # Hvis der er skrevet "standard" 
    # går den igang med at sorterer 100.000, 200.000, 300.000 og 400.000 tal
    for s in range(4):
        # Så udvælger den mængden af tal angivet i numGen variablen
        # i en liste fra 0-1.000.000 og sætter disse tal til at være i arrayet talliste
        talliste = random.sample(range(1000000), numGen)
        # Så printer den tallisten, hvor den er kørt igennem funktionen selection_sort
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
    # Så printer den tallisten, hvor den er kørt igennem funktionen selection_sort
    print(selection_sort(talliste))