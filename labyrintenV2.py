import time
import random

#jag tror inte arcade spelet funkar som det ska

picked_up_key = False
looked_at_map = False
map_introduction_text = False
picked_up_flashlight = False
won_aracde_game = False
inventory_lista = []

def clues_map():
        global looked_at_map
        global map_introduction_text
        if "Map" in inventory_lista:
              time.sleep(1)
              print("")
              house_layout()
              print("")
              time.sleep(1)
              if not map_introduction_text:
                print("\nIt looks like some sort of clues are drawn out on this map, maybe you should follow them.\n")
                map_introduction_text = True
                looked_at_map = True
def house_layout():
    text_house_layout = '''     
                    ___________________________
    ________________│∎∎∎∎∎∎∎∎∎∎∎∎│              │
    │_│✘│_│_│_│_│   │∎           ˂              │
    │____________   │∎          ∎│              │
    │  ✘          ˅ │✘          ∎│_________    _│
    │               │∎          ∎│          ︾
    │_____   ______ │____   _____│  
        │  ˅      ✘      ˅   │     
        │       ❘____❘       │_____
        │                    │     │
        │_____________    ___│_____│
                 │            │
                 │  Entrance  │
                 │____________│
                       ⬆'''
    print(text_house_layout)

def entrance(): #rum 1
    print("\nYou are at the entrance")
    print("What do you want to do") 
    entrance_decision()
def entrance_decision():
        global picked_up_key
        print("\n1) Open the door in front of you.")
        print("2) Wait a little.")
        if not picked_up_key:
            print("3) Turn around and try exit the bulding.")
        try:
            answer = int(input("\nYour choice: "))
        except ValueError:
            print("\nPlease enter a number.")
            time.sleep(1)
            entrance_decision()
        
        if answer == 1:
            print("\nYou approach the door ahead and open it.\n")
            time.sleep(2)

            reception()
        elif answer == 3:
            print("\nYou turn around and tug at the doorknob, but the door does not budge even the slightest...")
            print("You look around you and see a rusty key hanging on the clothes hanger to your left")
            
            rusty_key_decision()

        elif answer == 2:
            print("you have decided to stay for a while")
                
            for i in range(3):
                time.sleep(1)
                print(".", end="", flush=True) 
            time.sleep(2)
            print()
            entrance()
        else:
            print("\nPlease enter 1, 2 or 3.")
            entrance_decision()

def reception (): #rum 2
    print("You have entered the reception")
    print("\nThere is 1 door way over in the other side of the room to your left, one door slightly open straight ahead, and one door directly to your right\n")
    time.sleep(3)
    reception_door_choice()
def reception_door_choice():
    try:
        time.sleep(1)
        print("Enter the...")
        time.sleep(0.5)
        print("1) Door to your left.")
        time.sleep(0.5)
        print("2) Door straight ahead")
        time.sleep(0.5)
        print("3) Door to your right")
        time.sleep(0.5)        
        print("4) Go back to the entrance")
        time.sleep(1)
        print("\nOR")
        print("5) Show inventory")
        if "Map" in inventory_lista:
            print("6) Look at the map")
        time.sleep(1)
        global looked_at_map 
        if looked_at_map:
            print("\nCLUES")
            time.sleep(0.5)
            print("7) Go to the reception desk")
        question1 = int(input("\nYour choice: "))
    except ValueError:
        print("Please enter a valid number.")
        reception_door_choice()
    if question1 == 1:
         print("\nYou go up to the door and walk in...\n")
         time.sleep(1)
         gameroom()
    elif question1 == 2:
         print("Your mom")
    elif question1 == 3:
         print("Ahead you see a door with a keyhole on it.")
         try_keyhole()
    elif question1 == 4:
        entrance_decision()
    elif question1 == 5:
        time.sleep(1)
        print(f"\nInventory: {inventory_lista}\n")
        time.sleep(1)
        reception_door_choice()
    elif question1 == 6:
        clues_map()
        reception_door_choice()
    else:
         time.sleep(1)
         print("\nPlease enter one of the numbers displayed above")
         time.sleep(1)
         reception_door_choice()
            
def rusty_key_decision(): #At entrance
                try:
                    pick_up_key_question = int(input("\n1) Take the key \n2) Let it be\n\nYour choice: "))           
                except ValueError:
                    print ("\nPlease enter a valid number")
                    rusty_key_decision()
                global picked_up_key                
                if pick_up_key_question == 1:
                    picked_up_key = True
                    print ("\nYou take the key and put it in your pocket.")
                    time.sleep(1)
                    print ("\n    ˃ Item added to inventory! ˂")
                    inventory_lista.append("Rusty Key")
                    time.sleep(1.5)
                    print (f"\nInventory: {inventory_lista}")
                    print ("\nYou walk back to the entrance")

                    entrance_decision()
                elif pick_up_key_question == 2:
                    print("You decide to let the key hang where it is.")
                    print ("\nYou walk back to the entrance")
                    entrance_decision()
                else:
                    print("\nPlease enter 1 or 2")
                    rusty_key_decision()         
def hidden_key_room(): #room thats available after getting key at entrance
    time.sleep(1)
    print ("\nYou walk into the little room")
    time.sleep(1)
    print ("\nBefore you on some moldy shelves you see a map")
    time.sleep(1)
    pick_up_map_action()  
def pick_up_map_action ():
        try:
            question_pick_up_map = input("Pick up the map? Yes/no: ").lower()
        except ValueError:
            print("Please enter a valid answer")
            pick_up_map_action()
        if question_pick_up_map == "yes":
                    print ("\nYou take the map and put it in your pocket.")
                    time.sleep(1)
                    print ("\n    ˃ Item added to inventory! ˂")
                    inventory_lista.append("Map")
                    time.sleep(1.5)
                    print (f"\nInventory: {inventory_lista}")
                    print("\nYou back out into the reception")
                    reception_door_choice()
        elif question_pick_up_map == "no":
            print ("\nYou leave the map on the shelf and back out into the reception.")
            time.sleep(1.5)
            reception_door_choice()            
        else:
            print("\nPlease enter Yes or No\n")
            pick_up_map_action()       
def try_keyhole():
            if "Rusty Key" in inventory_lista:
                try:
                    question2 = input("Do you want to try use the key you found before? Yes/No: ").lower()
                except ValueError:
                    print("Please enter a valid answer")
                    try_keyhole()
                if question2 == "yes":
                    time.sleep(1)
                    print ("\n    ˃ Item removed from inventory ˂")
                    time.sleep(1)
                    inventory_lista.remove("Rusty Key")
                    time.sleep(1)
                    print(f"Inventory: {inventory_lista}")
                    time.sleep(1)
                    hidden_key_room()

                elif question2 == "no":
                    print("")
                else:
                    print("Please enter Yes or No")
                    try_keyhole()
            else:
                time.sleep(2)
                print("\nYou try the door but quickly realize that its locked.")
                time.sleep(1)
                print("\nYou go back")
                reception_door_choice()

def gameroom(): #rum 3
    print("\nYou have entered the gameroom.\n")
    time.sleep(0.5)
    gameroom_choice()
def gameroom_choice():
    print("What do you wanna do:")
    time.sleep(0.5)
    print("1) Walk to the half-open door at the far right of the room") #option 1
    time.sleep(0.5)
    print("2) Check out the billard table") #option 2
    time.sleep(0.5)
    print("3) Go back to the reception") #option 3
    time.sleep(0.5)
    print("\nOR")
    print("4) Show inventory") #option 4 
    if "Map" in inventory_lista:
        print("5) Look at the map") #option 5
    time.sleep(1)
    if looked_at_map:
        print("\nCLUES")
        print("6) Go to the arcade game in the left corner") #option 6
        time.sleep(0.5)
    try:
        question1 = int(input("\nYour choice: "))
    except ValueError:
        print("Please enter a valid number.")
        gameroom_choice()
    if question1 == 1: #Toilet stalls room
        print("You walk up to the door and peak into the room.")
        if not "Flashlight" in inventory_lista:
            print("But you cannot see anything due to there not being any light")
            print("Its better to return when you have something that can light up the dark")
            print("You walk back")
            time.sleep(1)
            gameroom_choice()
        if "Flashlight" in inventory_lista:
            print("You turn on your flashlight and enter the dark room...")
            toilet_stalls_room()
        else:
            print("You back away from the door...")
            gameroom_choice()
    elif question1 == 2: #Billard table
        print("You walk over to the billard table..")
        time.sleep(1)
        billard_table_action()
    elif question1 == 3: #Walk back
        print("You turn around and walk back.")
        reception()
    elif question1 == 4: #inventory
        print(f"\nInventory: {inventory_lista}")
        time.sleep(2)
        gameroom_choice()
    elif question1 == 5: #Map
        clues_map()
        gameroom_choice()
    elif question1 == 6: #If looked at map, arcade game
        print("You walk up to the Arcade game..")
        time.sleep(1)
        arcade_game_text()
    else:
        time.sleep(1)
        print("\nPlease enter one of the numbers mentioned above")
        time.sleep(1)
        gameroom_choice()
def billard_table_action():
    print("\nYou are standing in front of the billard table")
    try:
        question1 = int(input("\n1) Inspect the top of the table\n2) Look under the table\n3) Walk back\n")) #Desicions
    except ValueError:
        print("Please enter a number.")
        billard_table_action()
    if question1 == 1: #on top of the table
        print("You look on top of the table but nothing looks out of the ordinary...")
        time.sleep(1)
        billard_table_action()
    elif question1 == 2: #under billard table
        print("You bend down and look under the billard table...")
        time.sleep(0.5)
        global picked_up_flashlight
        if not picked_up_flashlight:
            print("You see a flashlight laying on the ground.")
            time.sleep(0.5)
            def pick_up_flashlight_action():
                try:
                    pick_up_flashlight_question = input("Pick up the flashlight? Yes/No: ").lower()
                except ValueError:
                    print("Please enter a valid answer.")
                    pick_up_flashlight_action()
                if pick_up_flashlight_question == "yes":
                    global picked_up_flashlight
                    picked_up_flashlight = True
                    print("You decide to pick up the flashlight")
                    print ("\n    ˃ Item added to inventory! ˂")
                    inventory_lista.append("Flashlight")
                    time.sleep(1.5)
                    print (f"\nInventory: {inventory_lista}")
                    print("You back away from under the table...")
                    billard_table_action()
                elif pick_up_flashlight_question == "no":
                    print("You let the flashlight lay there and back away from the table")
                    billard_table_action()
                else:
                    print("Please enter Yes or No\n")
                    pick_up_flashlight_action()
            pick_up_flashlight_action()
        if picked_up_flashlight:
            print("Theres nothing under the table...")
            time.sleep(1)
            billard_table_action()
    elif question1 == 3:
        print("You back away from the table.")
        time.sleep(1)
        gameroom_choice()
    else:
        print("Please enter one of the numbers mentioned above.")
        billard_table_action()

def toilet_stalls_room():
    global looked_at_map
    time.sleep(2)
    print("\nYou have entered the dark room that turns out to be the Bathroom.")    
    if not looked_at_map:
        print("But it doesnt seem like you know what to do in here...")
        time.sleep(1)
        print("\n1) Go back to the gameroom.")
        time.sleep(0.5)
        print("\nOR")
        print("5) Show inventory")
        if "Map" in inventory_lista:
            print("6) Look at the map")
        time.sleep(1)
        try:
            question1 = int(input("\nYour choice: "))
        except ValueError:
            print("Please enter a valid answer")
            toilet_stalls_room()
        if question1 == 1:
            gameroom()
        elif question1 == 5:
            time.sleep(1)
            print(f"\nInventory: {inventory_lista}\n")
            time.sleep(1)
            toilet_stalls_room()     
        elif question1 == 6:
            clues_map()
            toilet_stalls_room()       
    if looked_at_map:
        toilet_stalls_action()
def toilet_stalls_action():
    print("According to the map, youre supposed to walk to the 5th stall")
    try:
        question2 = int(input("What stall do you want to enter: "))
    except ValueError:
            print("Please enter a valid answer.")
            toilet_stalls_room()
    if question2 in [1,2,3,4,6]:
            print(f"You enter stall num.{question2}.")
            print("Theres nothing to see in here.")
            toilet_stalls_action()
    elif question2 == 5:
        toilet_map_piece_action()
    else:
        print("Theres not that many stalls.")
        toilet_stalls_action()
def toilet_map_piece_action():
    if not "Note: 7" in inventory_lista:
        print("In the 5th stall you can see a small note taped to the toilet lid.")
        time.sleep(1)
        print("You carefully remove the note from the lid and it reads: 0")
        print ("\n    ˃ Item added to inventory! ˂")
        inventory_lista.append("Note: 0")
        time.sleep(1.5)
        print (f"\nInventory: {inventory_lista}")
        time.sleep(2)
        print("You walk out of the bathroom")
        gameroom()
    else:
        print("Theres nothing to see in here.")
        print("You walk out of the bahroom")
        gameroom()

def arcade_game():
     global won_aracde_game
     print("Game START")
     time.sleep(1)
     antal_rätt=0
     num_of_guesses = 3
     while num_of_guesses > 0 and num_of_guesses <= 3:
        x_number = random.randint(1,10)
        y_number = random.randint(1,10)
        equation_Sum = x_number * y_number
        print("Whats the sum of...")
        time.sleep(0.5)
        print(f"{x_number} * {y_number} = ?")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
             print("Please enter a valid number.")
             time.sleep(1)
             arcade_game()
        if useranswer == equation_Sum:
             time.sleep(1)
             print("\nRätt! ")
             antal_rätt += 1
             print (f"\nAntal rätt: {antal_rätt}\n")
             num_of_guesses -= 1
             if antal_rätt == 3:
                  print("Good job.")
                  won_aracde_game = True
        elif useranswer != equation_Sum:
             print("Fel svar. Game Over")
             num_of_guesses -= 3
             print("\n1) Try again")
             print("2) Exit")
             question1 = int(input("\nYour choice: "))

                  
                  
        else:
             print("Something went wrong, Game Restarting...")
             time.sleep(2)
             arcade_game()



def arcade_game_text():
    print("You turn on the arcade game")
    print("After a few seconds you see the games name and rules displayed on the screen:")
    time.sleep(0.5)
    print("\n--------------------")
    time.sleep(0.5)
    print("|   THE MATH GAME  |")
    time.sleep(0.5)
    print("| Game:            |")
    time.sleep(0.5)
    print("| You will get 3   |")
    time.sleep(0.5)
    print("| math problems.   |")
    time.sleep(0.5)
    print("| Solve them all   |")
    time.sleep(0.5)
    print("| and get a prize. |")
    time.sleep(0.5)
    print("--------------------\n")
    arcade_game()


entrance()