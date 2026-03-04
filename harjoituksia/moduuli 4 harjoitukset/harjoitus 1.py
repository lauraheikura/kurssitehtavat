hinta = 5
rahaa_annettu = 0

while rahaa_annettu < hinta:
    rahaa_annettu += 1
    print("Rahaa annettu:", rahaa_annettu)

print("Kahvi maksettu.")

#-------------
hinta = 5
rahaa_annettu = 0

while True:
    rahaa_annettu += 1
    print("Rahaa annettu:", rahaa_annettu)

    if rahaa_annettu == hinta:
        break
print("Kahvi maksettu.")