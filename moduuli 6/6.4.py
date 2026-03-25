def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

#Pääohjelma testaus
luvut = [1, 2, 3, 4, 5]

tulos = laske_summa(luvut)

print(f"Listan lukujen summa on {tulos}")