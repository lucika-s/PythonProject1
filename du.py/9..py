
retazec = input("Zadaj reťazec: ")
pismeno = input("Zadaj písmeno, ktoré hľadáš: ")


if pismeno.lower() in retazec.lower():
    print(f"Písmeno '{pismeno}' sa nachádza v reťazci.")


    pocet = retazec.lower().count(pismeno.lower())
    print(f"Písmeno '{pismeno}' sa v reťazci nachádza {pocet} krát.")
else:
    print(f"Písmeno '{pismeno}' sa v reťazci nenachádza.")