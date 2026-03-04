while True:
    print("Valitse toiminto:")
    print("1 = Yhteenlasku")
    print("2 = Vähennyslasku")
    print("3 = Kertolasku")
    print("4 = Jakolasku")
    print("0 = Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "0":
        print("Ohjelma lopetetaan.")
        break

    elif valinta in ["1", "2", "3", "4"]:
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))

        if valinta == "1":
            tulos = luku1 + luku2
            print(f"Tulos on {tulos}")

        elif valinta == "2":
            tulos = luku1 - luku2
            print(f"Tulos on {tulos}")

        elif valinta == "3":
            tulos = luku1 * luku2
            print(f"Tulos on {tulos}")

        elif valinta == "4":
            if luku2 == 0:
                print("Nollalla ei voi jakaa.")
            else:
                tulos = luku1 / luku2
                print(f"Tulos on {tulos}")

    else:
        print("Virheellinen valinta.")