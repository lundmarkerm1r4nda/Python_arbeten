import random
import time

#lägg till en exit


def entrace(): #rum 1
    print("\nYou are at the entrance")
    print("what do you want to do")
    answer = input("\n1) go to the livingroom \n2) stay here\n3) Run straight through the livingroom into a room at the other side\n")

    if answer == "1":
        print("\nYou approach the door ahead and open it.\n")
        time.sleep(2)
        print("You have entered the livingroom")
        livingroom()

    elif answer == "2":
        print("you have decided to stay for a while")
        
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) 
        time.sleep(2)
        print()
        entrace()

    elif answer == "3":
        print("\nYou start running and stop right infront of a door where you can see sunlight looming out of...\n")
        time.sleep(2)
        sunny_room()

def livingroom():
    print("\nYou can see in front of you 2 doors.")
    time.sleep(1)
    print("From the door to your left you can see bright streaks of sunshine coming through.")
    time.sleep(0.5)
    print("From the door to your right you can feel a cold breeze.\n")
    time.sleep(1)
    answer = input("1) go back to the previous room, \n2) towards sunshine, \n3) towards the cold breeze.\n")
    
    if answer == "1":
        time.sleep(2)
        entrace()
    
    elif answer == "2":
        time.sleep(2)
        sunny_room()

    elif answer == "3":
        print("You walk toward the door to the chilly room...")
        time.sleep(2)
        chilly_room()

def sunny_room():

    print("You slowly open the door to the bright room and you're soon blinded to the point that you cannot see anything in front of you.\n")
    time.sleep(1)
    question1 = input("You can either:\n1) back out of the room into the livingroom \nOR\n2) Continue foward\n")

    if question1 == "1":
        print("\nYou decide to back out into the livingroom.")
        time.sleep(1)
        livingroom()
    
    else:
        print("\nYou continue foward.")
        print("\nSuddenly you can feel a thin string tightening in front of your ankles, and soon you hear the door behind you harashly close and lock.") 
        for i in range(5):
            time.sleep(1)
            print("-", end="", flush=True) 
        time.sleep(2)
        print("\nBut fear not, suddenly a little goblin pops up from under the woodboard.")
        print("\nGOBLIN: Beat me in a match of rock, papper and scissors and i will let you pass through!")

        question2=input("\nPlay a game against the Goblin? \n1) Yes\n2) No\n")

        if question2 == "2":
            print("\nDont be a coward.")
        
        print("\nYou decide to play a game against the goblin.")

        val = input("\nSten, Sax, Påse? ").lower()
        
        if val == "sten":
            print("\nGoblin chose Påse, you lost")
            print ("""
                -------------
                | GAME OVER |
                -------------  
                """)
        elif val == "påse":
            print("\nGoblin chose Påse, oavgjort")
            print ("""
                -------------
                | GAME OVER |
                -------------  
                """)
        else:
            print("\nGoblin chose Påse, you won!")
            time.sleep(0.5)
            print("And as promised, the goblin opens a door infront of you that you had not noticed.")
            long_corridor()
       
def chilly_room():
    time.sleep(1)
    print("\nyou squint your eyes to try to see through the thick layer of fog laying close to the floor.\n")
    question1 = input("You can either:\n1) This is way too dangerous, Back out of the room. \nOr\n2) Continue to inspect whats hiding under the fog\n")

    if question1 == "1":
        time.sleep(1)
        print("You back out of the room into the livingroom")
        time.sleep(1)
        livingroom()

    else:
        print("You continue to inspect the room")
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) 
        time.sleep(2)
        print("\nYou suddenly see whats the cause of the thick fog...\n")
        print("!!A big container full of ice cream has been installed to the floor, jippie!!\n") #placeholder
        print("You walk to the door at the end of the room and open it.")
        long_corridor()
     
def long_corridor():
    print("\nYou exit the room, and in front of you is a long dark corridor")
    question1 = input("\nDo u want to: \n1) Run through the corridor \nOR\n 2) Walk\n")
    if question1 == "1":
        print("You start sprinting through the corridor with everything you have.\n")
        print("Suddenly you feel a cold breath at your neck, this makes you run even faster...")
        time.sleep(1)
        print("Because you're running so fast you don't see the hole in the floor and suddenly the whole floor under you collapse and you fall into dark nothingness.")
        print ("""
            -------------
            | GAME OVER |
            -------------  
               """)
    
    else:
        print("\nYou start walking towards the end of the corridor which you cannot see")
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) 
        time.sleep(2)
        print("\nSuddenly the hair on your neck stands up and you can feel cold breath fanning over the back of your head")
        question2 = input("\n1) Run \nOR\n2) Continue walking\n")
        if question2 == "1":
            print("You start sprinting through the corridor with everything you have.\n")
            print("Because you're running so fast you don't see the hole in the floor and suddenly the whole floor under you collapse and you fall into dark nothingness.")
            print ("""
            -------------
            | GAME OVER |
            -------------  
                """)

        else:
            print("You withstand the urge to sprint away from the feeling an continue to walk.")
            for i in range(3):
                time.sleep(1)
                print(".", end="", flush=True) 
            time.sleep(2)
            print("\n\nAfter what feels like an enternity of walking you finally come to door.")
            print("You push the door open and enter the room")
            last_room()

def last_room():
    print("You are now in the room at the end of the corridor")
    print("You see a hole in the wall where u can see the sunlight shining on the other side, your freedom is close")
    question1 = input("\n1) Stay for a little longer\n2) Go through the hole to your freedom\n You want to: ")
    
    if question1 == "1":
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) 
        time.sleep(2)
        last_room()
    else:
        print("You run and jump through the hole...")
        print("""
        ------------
        | You Won! |
        ------------
                """)


print("""
      ---------------------------
      | Welcome to my Labyrinth |
      ---------------------------    
      """)
entrace()
