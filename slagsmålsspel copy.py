#Försök 2 

import random
import time

#problem - the money is not being saved, will always have 100 money in at the start.

while True: 

    randomnames = ('Bengt' , 'Peter' , 'Agatha')

    print ("\n================= Slagsmålsspelet =================\n")
    Player1 = input ("Name for player 1: ")
    Player2 = random.choice(randomnames)
    Player1Hp = 20
    Player2Hp = 20
    Money = 100

    print ("Finding your opponent...")
    time.sleep(3)
    print ("Opponent found, Your opponent is" , Player2)
        
    time.sleep(3)

    print ("\nYou currently have" , Money , "money.\n") 
    betting = input ("Do you want to place a bet? Yes/No\n").lower()
    if betting == "yes":
            while True:
                try: #för att man inte ska kunna skriva in annat än nummer
                    bettamount = float(input("How much do you money do you want to bet?\n"))
                    if bettamount > Money:
                        print ("Sorry you do not have enough money to bet that much.\n")
                    elif bettamount <= 0:
                        print ("The bet must be greater than 0, please try again.\n")
                    else:
                        print ("Bet placed, you bet", bettamount , "\n")
                        break
                    
                except ValueError:
                    print ("Invalid, please enter a number.\n")
    else:
        print ("\nNo bet placed.\n")
        time.sleep(2)

    while (Player1Hp >= 0 and Player2Hp >= 0):
        
        DamagePlayer1Basic = random.randint(1,7)
        DamagePlayer1Advanced = random.randint(10,20)
        DamagePlayer2Basic = random.randint(1,7)
        DamagePlayer2Advanced = random.randint(10,20)
        AdvancedChance = 0.4
        randomMoves = ('Basic' , 'Advanced' , 'Healing')
        Player2attack = random.choice(randomMoves)
        HealingPlayer1 = random.randint(3,5)
        HealingPlayer2 = random.randint(3,5)

        

        attack = input("Choose your attack:\nBasic (100% Hit-rate)\nAdvanced (40% Hit-rate)\nHealing (+3-5 HP)\n").lower()
        time.sleep(1)
        if attack == "basic":
            DamagePlayer1Basic
            print ("\n" , Player1, "made a" , attack , "attack.")
            print (Player2, "lost" , DamagePlayer1Basic , "HP\n")
            Player2Hp -= DamagePlayer1Basic

        if attack == "advanced":
            if random.random() < AdvancedChance:
                print ("\n" , Player1, "made an", attack , "attack")
                time.sleep(3)
                print (Player2, "lost " , DamagePlayer1Advanced , "HP\n")
                Player2Hp -= DamagePlayer1Advanced
            else:
                print("\n" , Player1 , "made and Advanced attack, it missed!" , Player2 , "took 0 damage")

        if attack == "healing":
            if Player1Hp >= 20:
                print ("\nHealing failed, HP is already +20\n")
            else:
                HealingPlayer1
                print ("\n" , Player1 , "healed up!\n")
                Player1Hp += HealingPlayer1
                print ("you gained" , HealingPlayer1 , "HP")
                print (Player1 , "currently has" , Player1Hp , "HP\n")

        time.sleep(1)
        print (Player2 , "currently has ", Player2Hp , "HP.\n")

        if Player2Hp <= 0:
            print (Player1, "won!\n")
            Money +=  bettamount * 2
            print ("You won the bet! Money currently in your possesion is" , Money , "\n")
            break

        time.sleep(3)

        print (Player2, "made a/n", Player2attack , "attack")


        if Player2attack == "Basic":
            DamagePlayer2Basic
            print (Player1, "took " , DamagePlayer2Basic , "HP\n" )
            Player1Hp -= DamagePlayer2Basic
            time.sleep(3)
            print (Player1 , "currently has " , Player1Hp , "HP\n")

        if Player2attack == "Advanced":
            if random.random() < AdvancedChance:
                DamagePlayer2Advanced
                print (Player1 , "took" , DamagePlayer2Advanced , "damage\n")
                Player1Hp -= DamagePlayer2Advanced
                time.sleep(3)
                print (Player1 , "currently has" , Player1Hp , "HP left\n")
            else:
                print (Player2 , "missed,", Player1 , "took 0 damage\n")
        
        if Player2attack == "Healing":
            if Player2Hp >= 20:
                print ("\nHealing failed, HP is already +20\n")
            
            else:
                HealingPlayer2
                print (f"\n{Player2} healed up! \n")
                Player2Hp += HealingPlayer2
                print (f"{Player2} currently has {Player2Hp} HP \n")


            time.sleep(3)

        if Player1Hp <= 0:
            print (f"{Player2} won!\n")
            Money -= bettamount
            print (f"You lost the bet, money in your possesion is currently:{Money}\n")
            break

        

    question = input("Play again? Yes/No:  ").lower()

    if question == "no":
        print ("Okej!")
        break






    


