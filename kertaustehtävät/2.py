tuntipalkka = float(input("Anna tuntipalkka:"))
tunnit = float(input("Anna tunnit:"))
viikonpaiva = input("Anna viikonpäivä:").lower()


viikonpaivat = "maanantai", "tiistai", "keskiviikko","torstai", "perjantai", "lauantai", "sunnuntai"

if viikonpaiva not in viikonpaivat:
    print("Virheellinen viikonpäivä.")
else:
    if viikonpaiva == "sunnuntai":
        paivapalkka = tuntipalkka * 2 * tunnit
    else:
        paivapalkka = tuntipalkka * tunnit

    print(f"Päiväpalkka: {paivapalkka} euroa.")