# Funktio
def suurin_arvo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Pääohjelma
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

suurin = suurin_arvo(luku1, luku2, luku3)

print(f"Suurin arvo on {suurin}")