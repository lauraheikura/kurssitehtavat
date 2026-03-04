tarina = ""
edellinen_sana = None
while True:
    sana = input("Anna sana lisättäväksi tarinaan:")

    if sana == "loppu":
        break
    if sana == edellinen_sana:
        break

    tarina += sana + " "
    edellinen_sana = sana

print(tarina)