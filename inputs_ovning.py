while True:
    Namn = input("Vad är ditt namn? ")
    Färg = input("Vilken är din favorit färg? ")
    Djur = input("Favorit djur? ")
    print( "Namn:", Namn, "Färg:", Färg, "Djur:", Djur)

    fråga = input("Stämmer det ja/nej? ")

    if fråga.lower() == "ja":
        break

    else:
        print("Okej, låt oss börja om!\n")

print(Namn , "hade en" , Färg , Djur)


