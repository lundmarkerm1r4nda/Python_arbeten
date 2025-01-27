#Ni ska skriva ett program som kör sten-sax-påse.
#Låt användaren bestämma hur många rundor som körs.
#Slumpa datorns val.
#Använd funktioner beroende på vilket val användaren har gjort (datorns val bör skickas med som parameter) (ex: sax(1), påse(1), sten(2) )
#Håll reda på hur många rundor användaren har vunnit och berätta hur många hen vunnit i slutet
import random

points = 0
ssp_lista = ["sten","påse","sax"]

def sten():
    global points
    print("Du valde sten.")
    if motståndare == "påse":
        print("Din motståndare valde Påse, Du förlorar.")
    elif motståndare == "sax":
        print("Din motståndare valde Sax, du vinner!")
        points += 1
        print(f"Du har {points} poäng.")
    else:
        print("Din motståndare valde sten, oavgjort!")

def sax():
    global points
    print("Du valde Sax.")
    if motståndare == "sten":
        print("Din motståndare valde Sten, Du förlorar.")
    elif motståndare == "påse":
        print("Din motståndare valde Påse, du vinner!")
        points += 1
        print(f"Du har {points} poäng.")
    else:
        print("Din motståndare valde Sax, oavgjort!")

def påse():
    global points
    print("Du valde Påse.")
    if motståndare == "sax":
        print("Din motståndare valde Sax, Du förlorar.")
    elif motståndare == "sten":
        print("Din motståndare valde Sten, du vinner!")
        points += 1
        print(f"Du har {points} poäng.")
    else:
        print("Din motståndare valde Påse, oavgjort!")

while True:
    print("Sten, sax eller påse?")
    print("1) Sten")
    print("2) Sax")
    print("3) Påse")

    motståndare = random.choice(ssp_lista)

    while True:
        try:
            actionchoice = int(input("Ditt val: "))
            break
        except ValueError:
            print("Please input a valid answer.")
    
    if actionchoice == 1:
        sten()
    
    elif actionchoice == 2:
        sax()
        
    elif actionchoice == 3:
        påse()
        

    question1=int(input("Spela igen? \n1) Ja \n2) Nej\n"))
    if question1 == 1:
            print("Ok")
    else:
        print("Stopping game")
        break