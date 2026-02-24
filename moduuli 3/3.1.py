pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print("Kuha on alamittainen.")
    print("Laske kuha takaisin järveen")
    print(f"Pituudesta puuttuu {puuttuu}cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallitun mittainen. Saat pitää kalan.")

