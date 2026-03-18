ostoslista = ["maito", "kananmuna", "juusto", "leipä", "leikkele"]
print("\nOSTOSLISTA:", ostoslista)


while ostoslista:
    tuote = input("Minkä tuotteen ostit:").lower()
    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("Jäjellä:", ostoslista)

    else:
        print("Tuote ei ostoslistalla.")

print("Ostokset suoritettu")