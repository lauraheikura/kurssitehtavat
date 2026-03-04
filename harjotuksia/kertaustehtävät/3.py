from math import sqrt

while True:
    numero = float(input("Anna kokonaisnumero:"))

    if numero == 0:
        break
    elif numero < 0:
        print("Virheellinen numero.")
    else:
        print(sqrt(numero))
