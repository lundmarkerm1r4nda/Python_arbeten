#Försök 2 

import random
import time

#problem - the money is not being saved, will always have 100 money in at the start.
money = 100
randomnames = ('Bengt' , 'Peter' , 'Agatha')

while True: 

    
    print ("\n================= Slagsmålsspelet =================\n")
    player1 = input ("Name for player 1: ")
    player2 = random.choice(randomnames)
    player1Hp = 20
    player2_hp = 20

    print ("Finding your opponent...")
    time.sleep(3)
    print ("Opponent found, Your opponent is" , player2)
        
    time.sleep(3)

    print ("\nYou currently have" , money , "money.\n") 
    betting = input ("Do you want to place a bet? Yes/No\n").lower()
    if betting == "yes":
            while True:
                try: #för att man inte ska kunna skriva in annat än nummer
                    bettamount = float(input("How much do you money do you want to bet?\n"))
                    if bettamount > money:
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

    while (player1Hp >= 0 and player2_hp >= 0):
        
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
            print ("\n" , player1, "made a" , attack , "attack.")
            print (player2, "lost" , DamagePlayer1Basic , "HP\n")
            player2_hp -= DamagePlayer1Basic

        if attack == "advanced":
            if random.random() < AdvancedChance:
                print ("\n" , player1, "made an", attack , "attack")
                time.sleep(3)
                print (player2, "lost " , DamagePlayer1Advanced , "HP\n")
                player2_hp -= DamagePlayer1Advanced
            else:
                print("\n" , player1 , "made and Advanced attack, it missed!" , player2 , "took 0 damage")

        if attack == "healing":
            if player1Hp >= 20:
                print ("\nHealing failed, HP is already +20\n")
            else:
                HealingPlayer1
                print ("\n" , player1 , "healed up!\n")
                player1Hp += HealingPlayer1
                print ("you gained" , HealingPlayer1 , "HP")
                print (player1 , "currently has" , player1Hp , "HP\n")

        time.sleep(1)
        print (player2 , "currently has ", player2_hp , "HP.\n")

        if player2_hp <= 0:
            print (player1, "won!\n")
            money +=  bettamount * 2
            print ("You won the bet! Money currently in your possesion is" , money , "\n")
            break

        time.sleep(3)

        print (player2, "made a/n", Player2attack , "attack")


        if Player2attack == "Basic":
            DamagePlayer2Basic
            print (player1, "took " , DamagePlayer2Basic , "HP\n" )
            player1Hp -= DamagePlayer2Basic
            time.sleep(3)
            print (player1 , "currently has " , player1Hp , "HP\n")

        if Player2attack == "Advanced":
            if random.random() < AdvancedChance:
                DamagePlayer2Advanced
                print (player1 , "took" , DamagePlayer2Advanced , "damage\n")
                player1Hp -= DamagePlayer2Advanced
                time.sleep(3)
                print (player1 , "currently has" , player1Hp , "HP left\n")
            else:
                print (player2 , "missed,", player1 , "took 0 damage\n")
        
        if Player2attack == "Healing":
            if player2_hp >= 20:
                print ("\nHealing failed, HP is already +20\n")
            
            else:
                HealingPlayer2
                print (f"\n{player2} healed up! \n")
                player2_hp += HealingPlayer2
                print (f"{player2} currently has {player2_hp} HP \n")


            time.sleep(3)

        if player1Hp <= 0:
            print (f"{player2} won!\n")
            money -= bettamount
            print (f"You lost the bet, money in your possesion is currently:{money}\n")
            break

        

    question = input("Play again? Yes/No:  ").lower()

    if question == "no":
        print ("Okej!")
        break






    


