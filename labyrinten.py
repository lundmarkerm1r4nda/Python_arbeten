import random
import time


def entrace(): #rum 1
    print("\nYou are at the entrance")
    print("what do you want to do")
    answer = input("\n1) go to the livingfroom \n2) stay here\n")


    if answer == "1":
        print("you approach the door ahead and open it.\n")
        time.sleep(2)
        print("You have entered the livingroom")
        livingroom()

    elif answer == "2":
        print("you have decided to stay for a while")
        
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) 
        time.sleep(2)
        entrace()

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
    question1 = input("You can either:\n1) back out of the room into the livingroom, or\n2) Continue foward\n")

    if question1 == "1":
        print("\nYou decide to back out into the livingroom.\n")
        time.sleep(1)
        livingroom()
    
    else:
        print("You continue foward.")
        print("Suddenly you can feel a thin string tightening in front of your ankles, and soon you hear the door behind you harashly close and lock.") 

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

print("""
      ---------------------------
      | Welcome to my labyrinth |
      ---------------------------    
      """)
entrace()
