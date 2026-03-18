varit = ["pinkki", "sininen", "vihreä", "punainen", "keltainen", "liila"]

lempivari = input("Mikä on lempivärisi?:").lower()

#Boolean muuttuja
loytyy = False

for var in varit:
    if lempivari == var:
        #Boolean muuttuja muutetaan todeksi
        loytyy = True

if loytyy:
    print("Löytyy listasta.")
else:
    print("Ei löydy listasta.")