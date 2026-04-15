lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoasema")
    print("0 = Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "0":
        print("Ohjelma lopetetaan.")
        break

    elif valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()

        if icao in lentoasemat:
            print(f"Lentoaseman nimi on: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    else:
        print("Virheellinen valinta.")