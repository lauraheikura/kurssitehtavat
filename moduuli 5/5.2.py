luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa):")
    if syote == "":
        break
    luku = float(syote)
    luvut.append(syote)
if luvut:
    luvut.sort(reverse=True)

    print("Viisi suurinta lukua:")
    for luku in luvut [:5]:
        print(luku)
else:
    print("Lukuja ei annrttu.")