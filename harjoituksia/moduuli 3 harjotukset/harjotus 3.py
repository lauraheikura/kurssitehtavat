raha=float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Tässä kahvisi ole hyvä!")
else:
    puuttuva = 5 - raha
    print("Sorry, sinulta puuttuu", puuttuva)

print("Kiitos hei!")