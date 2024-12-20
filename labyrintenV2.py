import time

inventory_lista = []

def back_at_entrance_decision(): #Entrance function after key have been picked up
                        print("You are back at the entrance.")
                        try:
                            question1 = int(input("\n1) Open the door in front of you.\n2) Wait a little.\n"))
                        except ValueError:
                            print("\nPlease enter a valid number.")
                            back_at_entrance_decision()
                        if question1 == 1:
                            print("\nYou open the door in front of you..")
                            livingroom()
                        elif question1 == 2:
                            print("\nYou have decided to stay for a while")
                
                            for i in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True) 
                            time.sleep(2)
                            print()
                            back_at_entrance_decision()
                        else:
                            print("\nPlease enter 1 or 2")
                            back_at_entrance_decision()
def rusty_key_decision():
                try:
                    pick_up_key_question = int(input("\n1) Take the key \n2) Let it be\n"))           
                except ValueError:
                    print ("\nPlease enter a valid number")
                    rusty_key_decision()
                if pick_up_key_question == 1:
                    print ("\nYou take the key and put it in your pocket.")
                    time.sleep(1)
                    print ("\n    ˃ Item added to inventory! ˂")
                    inventory_lista.append("Rusty Key")
                    time.sleep(1.5)
                    print (f"\nInventory: {inventory_lista}")
                    print ("\nYou walk back to the entrance")

                    back_at_entrance_decision()
                elif pick_up_key_question == 2:
                    print("You decide to let the key hang where it is.")
                    print ("\nYou walk back to the entrance")
                    back_at_entrance_decision()
                else:
                    print("\nPlease enter 1 or 2")
                    rusty_key_decision()
def entrance_decision():
        try:
            answer = int(input("\n1) Open the door in front of you.\n2) Turn around and try exit the bulding.\n3) Wait a little.\n"))
        except ValueError:
            print("\nPlease enter a number.")
            time.sleep(1)
            entrance_decision()
        
        if answer == 1:
            print("\nYou approach the door ahead and open it.\n")
            time.sleep(2)

            livingroom()
        elif answer == 2:
            print("\nYou turn around and tug at the doorknob, but the door does not budge even the slightest...")
            print("You look around you and see a rusty key hanging on the clothes hanger to your left")
            
            rusty_key_decision()

        elif answer == 3:
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

def livingroom_door_choice():
    try:
        question1 = int(input("Enter the..\n1) Door to your left\n2) Door straight ahead\n3) Door to your right\n4) Go back to the entrance\n"))
    except ValueError:
        print("Please enter a valid number.")
        livingroom_door_choice()
    if question1 == 1:
         print("YOu are a rat")
    elif question1 == 2:
         print("Your mom")
    elif question1 == 3:
         print("Ahead you see a door with a keyhole on it.")
         try_keyhole()
    elif question1 == 4:
         if "Rusty Key" in inventory_lista:
              back_at_entrance_decision()
         else:
              entrance()
    else: 
        print("Please enter 1, 2, 3 or 4")       
        livingroom_door_choice()   
def try_keyhole():
            if "Rusty Key" in inventory_lista:
                try:
                    question2 = input("Do you want to try use the key you found before? Yes/No:").lower()
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

                elif question2 == "no":
                    print("")
                else:
                    print("Please enter Yes or No")
                    try_keyhole()
            else:
                print("You try the door but quickly realize that its locked.")
                print("You go back")
                livingroom_door_choice()


def entrance(): #rum 1
    print("\nYou are at the entrance")
    print("What do you want to do") 
    entrance_decision()

def livingroom (): #rum 2
    print("You have entered the livingroom")
    print("\nThere is 1 door way over in the other side of the room to your left, one door slightly open straight ahead, and one door directly to your right")
    time.sleep(3)
    livingroom_door_choice()


entrance()

'''
inventory_lista = []

print("Du går in i ett rum, på golvet ligger en nyckel")
fråga1 = input("Ta upp nyckeln? Ja/Nej: ").lower()

if fråga1 == "ja":
    inventory_lista.append("Rusty Key")

    print(inventory_lista)

else:
    print("You decided to not pick up the key, you suck.")
    print(inventory_lista)
'''

house_layout = '''     
                ___________________________
________________│           │              │
│_│_│_│_│_│_│  │           ˂               │
│____________  │            │              │
  │           ˅│            │______________│
  │            │            │
  │_____   ____│____   _____│
      │  ˅           ˅     │
      │                    │_____
      │                    │     │
      │____________   _____│_____│
               │    ˅     │
               │          │
               │__________│
                       ⬆'''