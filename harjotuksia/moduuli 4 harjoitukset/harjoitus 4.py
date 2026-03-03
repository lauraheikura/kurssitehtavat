kasky = input("Annetaanko lisää kolikoita?")

while kasky != "ei":
    if kasky == "ryöstö":
        print("Kolikot ryöstetty.")
        break
    print("Annetaan kolikko.")
    kasky = input("Annetaanko lisää kolikoita?")
else:
    print("Hyvästi!")

print("Ohjelma loppuu.")