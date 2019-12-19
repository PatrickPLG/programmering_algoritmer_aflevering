def selection_sort():

    # Der oprettes et array af tal ved navn tallist
    # og en variabel n som er længden af tallist
    tallist = [2, 4, 5, 1, 3, 6, 9, 8, 7]
    n = len(tallist)

    # Der oprettes en løkke i som er længden af tallisten -1
    for i in range(n-1):
        # mini variablen sættes til at være i
        mini = i

        # Der oprettes en løkke j
        # som længden mellem variablen i +1 til længden af n
        for j in range(i + 1, n):
            # Hvis tallist[j] er mindre end tallist[mini]
            # sættes mini til at være j
            if tallist[j] < tallist[mini]:
                mini = j
        # Hvis mini ikke er lig med i
        # bytter den om på tallist[mini] og tallist[i]
        if mini != i:
            tallist[mini],tallist[i] = tallist[i], tallist[mini]
    # Resultatet af den sorterede tallist skrives i terminalen
    return tallist

# Printer funktionen selection_sort
print(selection_sort())
