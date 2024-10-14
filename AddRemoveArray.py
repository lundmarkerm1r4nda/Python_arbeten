dogs = ["Fido" , "Spot" , "Scooby"]

new_dog = input("What is the name of the new dog?\n")

dogs.append(new_dog)

print(f"the dogs currently at the daycare are {dogs}")

leaving_dog = input("Who is leaving the daycare?\n")

dogs.remove(leaving_dog)

