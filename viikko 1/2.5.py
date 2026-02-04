leiviskat = int(input("Anna leiviskat:"))
naulat = int(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

# Muunnetaan kaikki luodeiksi
luodit_yhteensa = ( leiviskat * 20 * 32 + naulat * 32 + luodit )

# Muunnetaan grammoiksi
grammat_yhteensa = luodit_yhteensa * 13.3

# Kilot ja grammat
kilot= int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000

print(f"Massa on {kilot} kg ja {grammat:.1f}g")