def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

#Pääohjelma
while True:
    maara = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))

    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print(f"{maara} gallonaa on {litrat:.3f} litraa.")