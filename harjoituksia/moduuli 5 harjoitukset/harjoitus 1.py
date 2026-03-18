varit = ["pinkki", "sininen", "vihreä", "punainen", "keltainen", "liila"]

lempivari = input("Mikä on lempivärisi?:").lower()

if lempivari in varit:
    print("Väri löytyi listasta.")
else:
    print("Väriä ei löytynyt listasta")
