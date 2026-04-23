henkilot = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}

# Tulostukset
print(henkilot["John"][0], henkilot["John"][1])  # nimi ja ikä
print(henkilot["Emily"][2])  # ammatti

# Muokkaus
henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]

# Lisäys
henkilot["Sophia"] = ["Sophia", 35, "Lääkäri"]

# Poisto
del henkilot["Emily"]

print(henkilot)