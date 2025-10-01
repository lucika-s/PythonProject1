import math  # kvoli odmocnine

a = float(input("Zadaj a: "))
b = float(input("Zadaj b: "))
c = float(input("Zadaj c: "))


if a == 0: #ak by bolo a = 0 tak je to lineárna rovnica
    # Lineárna rovnica alebo žiadne riešenie
    if b != 0:
        x = -c / b
        print(f"Rovnica je lineárna, koreň: x = {x}")
    else:
        if c != 0:
            print("Rovnica nemá riešenie")
        else:
            print("Rovnica má nekonečne veľa riešení")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Rovnica má dva reálne korene: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Rovnica má jeden dvojnásobný koreň: x = {x}")
    else:
        print("Rovnica nemá reálne korene")
