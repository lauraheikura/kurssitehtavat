sanat = ["kettu", "possu", "koira", "kissa", "kirahvi", "kala", "hamsteri"]

laskuri = 0
pitka_sana = []

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1
        pitka_sana.append(sana)

print(f"Sanoja, joissa on yli 5 kirjainta: {laskuri}")
print("Sanat ovat:")
for sana in pitka_sana:
    print(sana)
