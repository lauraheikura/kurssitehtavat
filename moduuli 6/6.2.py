import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

#Pääohjelma
tahkot = int(input("Anna nopan tahkojen maksimisilmäluku: "))

while True:
    silmaluku = heita_noppa(tahkot)
    print(f"Sait luvun: {silmaluku}")

    if silmaluku == tahkot:
        break