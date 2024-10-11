#• Minst en klasskamrat ska ha testat din berättelse & ha tittat på koden.

ascii_title = """
  _______ _            ____                 _     __          _                     _    _                       
 |__   __| |          |  _ \               | |   / _|        | |                   | |  | |                      
    | |  | |__   ___  | |_) |_ __ ___  __ _| | _| |_ __ _ ___| |_   _ __ ___  _   _| | _| |__   __ _ _ __   __ _ 
    | |  | '_ \ / _ \ |  _ <| '__/ _ \/ _` | |/ /  _/ _` / __| __| | '_ ` _ \| | | | |/ / '_ \ / _` | '_ \ / _` |
    | |  | | | |  __/ | |_) | | |  __/ (_| |   <| || (_| \__ \ |_  | | | | | | |_| |   <| |_) | (_| | | | | (_| |
    |_|  |_| |_|\___| |____/|_|  \___|\__,_|_|\_\_| \__,_|___/\__| |_| |_| |_|\__,_|_|\_\_.__/ \__,_|_| |_|\__, |
                                                                                                            __/ |
                                                                                                           |___/ """

print (ascii_title)

print ("\nYou wake up hastily from what must've been a nightmare, sweaty and stressed you look around your room and try to calm yourself")
start_the_day = input ("\nAfter what feels like an eternity of trying to fall asleep, should you stop trying and start the day? Yes/No\n").lower()
if start_the_day == "yes":
    print ("\nYou go down to the kitchen...")
else: #Sleep more option
    print ("\nYou try for 30 more minutes. But sleep does not come your way and you decide to go down to the kitchen anyways.")
  
breakfast = input("\nIn the kitchen another choice awaits you. Bread or Yoghurt for breakfast?\n").lower()
if breakfast == "bread":
    print ("\nYou walk to the cupboard to pick bread")
    bread_type = input("Sourdough or Wholewheat?\n").lower()
    if bread_type == "sourdough":
        print ("\nYou take out the Sourdough and cut 2 slices.")
    else: #Wholewheat option
        print ("\nYou take out the Wholewheat and cut 2 slices.")

    print(f"\nYou spread butter on your {bread_type} slices")

    bread_toppings = input("\nYou open the fridge to see what toppings options you have. Cheese or Ham?\n").lower()
    if bread_toppings == "cheese":
        print("\nYou take out the Cheese and also the slicer next to it. You cut 2 thin slices for each bread slice.")
    else: #Ham option
        print("\nYou open the container and take out one piece of Ham for each slice of bread.")

    print(f"\nYou take your {bread_type} slices with {bread_toppings} and go sit down at the table.")

else:
    yoghurt_flavor = input("\nYou walk to the fridge. What flavor Yoghurt do you want? Mango or Banana\n").lower()
    if yoghurt_flavor == "mango":
        print ("\nYou take out the Mango Flavored Yoghurt and pours it down into your bowl")
    else: #Banana option
        print ("\nYou take out the Banana Flavored Yoghurt and pours it into your bowl.")
    print (f"After pouring the {yoghurt_flavor} yoghurt into your bowl you are left to decide what cereal to have.")
    cereals = input("Musli or Cornflakes?\n").lower()

    if cereals == "musli":
        print(f"\nYou shake the Musli down on top of your {yoghurt_flavor} yoghurt.")
    else: #cornflakes option
        print(f"\nYou walk to the cupboard to take out the Cornflakes, you open the door but get jumped by a rat, turns out the rat has been sitting in here snacking on your cornflakes. But you take the cornflakes that are left and pours them on your {yoghurt_flavor} yoghurt.")

    print(f"You take your {yoghurt_flavor} {breakfast} with {cereals} and go sit down at the table.")

