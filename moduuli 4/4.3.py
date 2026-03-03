ensimmainen = input("Anna luku (tyhjä lopettaa):")

if ensimmainen == "":
    print("Lukuja ei annettu.")
else:
    pienin = suurin = float(ensimmainen)

    while True:
        syota = input("Anna luku (tyhjä lopettaa):")

        if syota == "":
            break

        luku = float(syota)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku


    print(f"Pienin luku: {pienin} ")
    print(f"Suurin luku: {suurin} ")

