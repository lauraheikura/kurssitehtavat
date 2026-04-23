kirjasto = {
    "Kirja1": ["Kirjailija1", 2000, "Romaani"],
    "Kirja2": ["Kirjailija2", 2010, "Scifi"]
}

print(kirjasto["Kirja1"][0])  # kirjoittaja
print(kirjasto["Kirja2"][2])  # genre

# Muutos
kirjasto["Kirja1"][2] = "Draama"

# Lisäys
kirjasto["Kirja3"] = ["Kirjailija3", 2020, "Fantasia"]

# Poisto
del kirjasto["Kirja2"]

print(kirjasto)