#Försök 1

import random
import time

while True: 

    randomnames = ('Bert' , 'Kurt' , 'Berit')

    print ("\n================= Slagsmålsspelet =================\n")
    Player1 = input ("Name for player 1: ")
    Player2 = random.choice(randomnames)
    Player1Hp = 20
    Player2Hp = 20

    print ("Finding your opponent...")
    time.sleep(3)
    print ("Opponent found, Your opponent is" , Player2)

    time.sleep(3)

    while (Player1Hp >= 0 and Player2Hp >= 0):
        DamagePlayer1 = random.randint(1,20)
        DamagePlayer2 = random.randint(1,20)

        print (Player1, "hit " , Player2)
        
        Player2Hp -= DamagePlayer2

        print (Player2 , "lost ", DamagePlayer2 , "HP")
        if DamagePlayer2 == 20:
            print ("Critical hit!")

        print (Player2 , "currently has ", Player2Hp , "HP.")

        if Player2Hp <= 0:
            print (Player1, "won!")
            break

        time.sleep(3)

        print (Player2, "hit ", Player1)

        Player1Hp -= DamagePlayer1

        print (Player1, "lost ", DamagePlayer1, "HP ")
        if DamagePlayer1 == 20:
            print ("Critical hit!")    
        
        print (Player1, "currently has ", Player1Hp, "HP.")

        if Player1Hp <= 0:
            print (Player2, "won!")
            break

        time.sleep(3)

    question = input("Play again? Yes/No:  ").lower()

    if question == "no":
        print ("Okej!")
        break






    


