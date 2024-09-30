#Försök 3, försökte göra det mer avancerat än försök 2 men det tog stopp. Koden funkar inte

import random
import time

while True: 

    randomnames = ('Lars' , 'Boris' , 'Freya')

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
        
        randomMoves = ('Basic' , 'Advanced' , 'Healing')
        Player2attack = random.choice(randomMoves)
        skills = ()
        
        HealingPlayer2 = random.randint(3,5)

        def basic(Player2Hp):
            basic_dmg = random.randint(1,10)
            Player2Hp -= basic_dmg
            if basic_dmg >= 1 and basic_dmg <= 10:
                print(f"{Player1}, smacked {Player2} with their fist, {Player2} took {basic_dmg} damage.")
            if basic_dmg == 1:
                print(f"Critical miss,{Player2} took {basic_dmg} damage.")
            if basic_dmg == 10:
                print(f"Critical hit, {Player2} took {basic_dmg} damage!")
            return Player1Hp
            
        def Advanced(Player2Hp):
            Advanced_dmg = random.randint(10,20)
            Advanced_chance = 0.40
            if random.random() < Advanced_chance:
                Player2Hp -= Advanced_dmg
                if Advanced_dmg !=20:
                    print(f"{Player1}, swung their fist with all they had, {Player2} took {Advanced_dmg} damage.")
                if Advanced_dmg == 20:
                    print(f"Critical hit! {Player1} swung their fist so hard that {Player2} took {Advanced_dmg}damage!")
            else:
                print(f"{Player1} missed! {Player2} took 0 damage.")
            return Player2Hp
        
        def Healing(Player1Hp):
            Healing_amount = random.randint(5,10)
            Healing_amount += Player1Hp
            print(f"{Player1} healed up, you gained {Healing_amount} HP")
            return Player1Hp
        
        def kick(Player2Hp):
            kickdamage1 = random.randint (5-10)
            kickdamage2 = random.randint (5-10)
            kick_chance1 = 0.90
            kick_chance2 = 0.50
            if random.random() < kick_chance1:
                Player2Hp -= kickdamage1
                if random.random() < kick_chance2:
                    Player2Hp -= kickdamage2
                    print (f"{Player1} did a roundabout and landed both hits {Player2}, {Player2} took {kickdamage1} and {kickdamage2} damage!")
                else:
                    print(f"{Player1} did a roundabout and landed one hit {Player2}, took {kickdamage1} damage.")
            else:
                print(f"{Player1} tried to kick {Player2}, it did not work. {Player2} took 0 damage.")

        def all_out(Player2Hp):
            all_out_damage = 100
            all_out_chance = 0.10
            if random.random() < all_out_chance:
                Player2Hp -= all_out_damage
                print(f"Critical Hit! {Player1} channeled their inner beast and one-shotted {Player2}!")
            else:
                print(f"{Player1} tried to be Alpha, but it didnt work. {Player2} took 0 damage.")

        Available_moves = (basic,Advanced,Healing,kick,all_out)

        Player1ATK = 10
        Player1DEF = 10
        Player2ATK = 10
        Player2DEF = 10

        print (Player1 , "\n" "\nHP:" , Player1Hp , "\nAttack:" , Player1ATK , "\nDefense" , Player1DEF )
        print ("")
        print ("")


        print (f"-----------------   --------------------\n1. Basic attack      2. Advanced attack\nDamage: 1-10            Damage: 10-20\nAccuracy: 100%          Accuracy: 40%\n-----------------   --------------------")
        print (f"3. Healing           4. All Out\nAmount: 5-10            Damage: 100\nAccuracy: 100%          Accuracy: 10%\n-----------------   --------------------")
        print (f"5. Kick\nAttribute: Your player does damage twice 5-10(x2)\nAccuracy: 1st 90% 2nd 50%\n-----------------   --------------------")
        chosen_moves = int(input(f"Please choose 3 moves out of these 5 to use during your battle (1-5):"))

        if chosen_moves == "1":
                skills + basic , Advanced
                print("you have chosen the Basic skill.")

        print(skills)
        

        
            

        


        break


        
        
    Player1_
    
    question = input("Play again? Yes/No:  ").lower()

    if question == "no":
        print ("Okej!")
        break






    


