from datetime import date

rok = int(input("Zadaj rok narodenia: "))
mesiac = int(input("Zadaj mesiac narodenia: "))
den = int(input("Zadaj deň narodenia: "))

dnes = date.today()

narodenie = date(rok, mesiac, den)


if dnes.year - narodenie.year >=18:
    print("Je plnoletý")
else:
    print("Nie je plnoletý")
