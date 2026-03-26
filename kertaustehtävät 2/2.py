arvot = []

while True:
    syote = int(input("Anna arvo (0 lopettaa):"))
    if syote == 0:
        print("Heippa!")
        break

    arvot.append(syote)
    print("Lista nyt:", arvot)

    jarjestetty = sorted(arvot)
    print("Lista järjestyksessä:", jarjestetty)

