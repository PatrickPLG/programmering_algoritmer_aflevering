# https://www.geeksforgeeks.org/sorting-algorithms/

# Vi har valgt at arbejde med algoritmen Gnome sort

# Gnome sort virker ved, at den først tjekker det første tal i tallitsten (position 0) og om der er et tal før det.
# Da der ikke er et tal før, rykker Gnome sort 1 position frem og tjekker om der er et tal før.
# Der er et tal før, men da det er mindre end position 1, går den videre.
# Den går så videre og tjekker for tallet i position 2, tallet i position 2 er så mindre end position 1.
# Gnome sort bytter så de to tal så det mindre tal nu er på position 1. Derefter tjekker den, om position 1 er mindre en position 0.
# Position 0 er mindre end position 1. Derfor går koden bare videre til næste tal i rækken, nemlig position 3.
# Sådan går den frem og tilbage hele tiden, indtil tallisten er blevet sorteret.
 

def gnome_sort(A):
    # opretter en varibel, pos, og sætter den lig med 0
    pos = 0
    # tjekker om pos er mindre end længden af A
    while pos < len(A):
        # hvis at pos er lig med 0 eller pos er større end eller lig med pos-1
        # plusser den pos med 1
        if (pos == 0 or A[pos] >= A[pos-1]):
            pos = pos + 1
        else:
            # bytter om på pos og pos-1 og rykker pos 1 tilbage
            A[pos], A[pos-1] = A[pos-1], A[pos]
            pos = pos-1
    # returnere A
    return A


# Tallisten som algoritmen skal sortere
talliste = [4, 312, 12, 312, 3, 1, 23, 1, 5, 2, 312, 31, ]
# Tallisten inden sortering
print(talliste)
# Tallisen efter sortering
print(gnome_sort(talliste))
