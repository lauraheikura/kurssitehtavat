import random

maara = int(input("Kuinka monta arpakuutiota heitetään?:"))

summa = 0

for i in range(maara):
    silmaluku= random.randint(1,6)
    print(f"Noppa {i+1}: {silmaluku}")
    summa += silmaluku

print(f"Silmälukujen summa on {summa}.")