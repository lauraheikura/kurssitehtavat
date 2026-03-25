import math

def yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala

#Pääohjelma
print("Anna ensimmäisen pizzan tiedot.")
d1 = float(input("Halkaisija (cm): "))
h1 = float(input("Hinta (€): "))

print("\nAnna toisen pizzan tiedot:")
d2 = float(input("Halkaisija (cm): "))
h2 = float(input("Hinta (€): "))

# Lasketaan yksikköhinnat
y1 = yksikkohinta(d1, h1)
y2 = yksikkohinta(d2, h2)

print(f"\nPizzan 1 yksikköhinta: {y1:.2f} €/m²")
print(f"Pizzan 2 yksikköhinta: {y2:.2f} €/m²")

# Verrataan
if y1 < y2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif y2 < y1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")