import random

def kollasax():
    motstandare =random.choice(ssp)
    print(f"du valde {val}")
    print (f"din motståndare valde {motstandare}")
    if ssp == "sax":
        print("oavgjort")

    elif motstandare == "sten":
        print("du har förlorat")

    else:
        print("du vann")


val = input("sten, sax, påse? ").lower()
ssp=["sten","sax","påse"]

if val == "sax":
    kollasax

