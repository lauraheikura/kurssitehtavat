import random

# Kolmenumeroinen koodi, numerot 0..9
koodi3 = ""
for _ in range(3):
    koodi3 += str(random.randint(0, 9))

# Nelinumeroinen koodi, numerot 1..6
koodi4 = ""
for _ in range(4):
    koodi4 += str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi (0-9): {koodi3}")
print(f"Nelinumeroinen koodi (1-6): {koodi4}")