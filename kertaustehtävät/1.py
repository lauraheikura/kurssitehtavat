nimi = input("Kerro nimesi:")


if nimi != "Matti":
    annokset = int(input("Kuinka monta keittoannosta?"))
    hinta = annokset * 5.90
    print (f"Kokonaishinta on {hinta}.")
    print ("Seuraava kiitos!")
else:
    print("Seuraava, kiitos!")

