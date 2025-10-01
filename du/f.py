x = input("Zadaj znak: ")

if x.lower() in "aeiou": print("Samohláska")
elif x.isalpha(): print("Spoluhláska")
elif x.isdigit(): print("Číslica")
elif x in "+-*/": print("Znak operácie")
else: print("Niečo iné")

