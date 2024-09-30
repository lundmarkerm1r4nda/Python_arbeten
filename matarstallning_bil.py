# Räkna ut bensin förbrukning per mil på ett år

mil2 = int(input("Mätarställning Idag? "))
mil1 = int(input("Mätarställning för ett år sedan? "))

while (mil1 > mil2):
    print("Fel, mätarställning angiven")
    mil2 = int(input("Mätarställning Idag? "))
    mil1 = int(input("Mätarställning för ett år sedan? "))

print("Antal körda mil: ", mil2 - mil1)
liter = float(input("Antal liter bensin "))
print(f"Förbrukning per mil: {liter/(mil2-mil1):.2f}")


