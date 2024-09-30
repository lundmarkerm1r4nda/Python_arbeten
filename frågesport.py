#Skapa en frågesport med minst tre frågor.
#För varje fråga ska spelaren få välja mellan tre olika alternativ.
#Tips: det blir mycket enklare om hen får skriva in “a, b eller c” eller “1, 2 eller 3” snarare än kompletta svar.

#Spelet ska hålla reda på antalet rätta svar, i en variabel.
#I slutet av spelet ska spelaren få veta sitt resultat.

import time

points = 0

print ("Vad blir 14+7?")
time.sleep(1)
print ("A:21")
print ("B:25")
print ("C:19")
answer1 = input("Svar: ")

if answer1 == "A":
    points +=1

print ("Vad blir 92+50?")
time.sleep(1)
print ("A:245")
print ("B:142")
print ("C:130")
answer1 = input("Svar: ")

if answer1 == "B":
    points +=1

print ("Vad blir 10297+17895?")
time.sleep(1)
print ("A:27568")
print ("B:29412")
print ("C:28192")
answer1 = input("Svar: ")

if answer1 == "C":
    points +=1


print ("Du fick: ")
print (points , "poäng")
