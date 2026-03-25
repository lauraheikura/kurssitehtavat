import random

def heita_noppa():
    return random.randint(1, 6)

#Pääohjelma
while True:
    silmaluku = heita_noppa()
    print(f"Sait luvun: {silmaluku}")

    if silmaluku == 6:
        break