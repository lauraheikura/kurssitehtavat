oppilaat = {
    "Matti": ["Matti", 7, "Matematiikka"],
    "Liisa": ["Liisa", 8, "Biologia"]
}

print(oppilaat["Matti"][1])  # vuosiluokka
print(oppilaat["Liisa"][2])  # lempiaine

# Muutos
oppilaat["Matti"][2] = "Fysiikka"

# Lisäys
oppilaat["Pekka"] = ["Pekka", 6, "Historia"]

# Poisto
del oppilaat["Liisa"]

print(oppilaat)