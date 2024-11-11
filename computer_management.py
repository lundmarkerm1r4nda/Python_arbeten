import time

#Behövs: Arrays, Len(), count, while, for, it
#wat do you wanna do, add, or send pc
#Fixa info för datorn

available_computers = ["2020","2021","2022","2023"]
on_service_computers = ["2017","2018","2019"]

while True: 
    task = input(f"""\n    What do you want to do?
    1. Move Computer TO Service
    2. Move Computer FROM Service
    3. Add new computer
    4. Remove old computer
    -  Exit\n""").lower()
    
    if task == "1":
        while True:
            time.sleep(1)
            print(f"\nAvailable computers: {available_computers}\n")
            time.sleep(2)
            to_service_computers = input("What computer is going to Service?\n")
            print(f"\nMoving {to_service_computers} to Service.\n")
            time.sleep(1)
            available_computers.remove(to_service_computers)
            on_service_computers.append(to_service_computers)
            print(f"\nComputers on Service: {on_service_computers}")
            print(f"Available Computers: {available_computers}")
            break
            
    elif task == "2":
        while True:
            time.sleep(1)
            print(f"Computers at Service: {on_service_computers}\n")
            time.sleep(2)
            from_service_computer = input("What computer is done at service?\n")
            print(f"\nMoving {from_service_computer} to Available computers.\n")
            time.sleep(1)
            on_service_computers.remove(from_service_computer)
            available_computers.append(from_service_computer)
            print(f"\nComputers on Service: {on_service_computers}")
            print(f"Available Computers: {available_computers}")
            break

    elif task ==  "3":
        while True:
            time.sleep(1)
            name_of_new_computer = input(f"\nName of the computer: ")
            owner_of_computer = input(f"\nWho has the computer: ")
            last_serviced = input(f"\nLast serviced: ")

            available_computers.append(name_of_new_computer)

            print (f"""\n
            Computer: {name_of_new_computer}
            Owner: {owner_of_computer}
            Serviced: {last_serviced}\n""")

            print (f"Available computers: {available_computers}")

            break

    elif task == "4":
        while True:
            try:
                time.sleep(1)
                remove_old_computer = input(f"\nName of computer: ")
                available_computers.remove(remove_old_computer)
                
                print (f"\n{remove_old_computer} has been removed.")
                print (f"""\n
                Available computers: {available_computers}
                Computers on service: {on_service_computers}""")
                time.sleep(1)
                break
            except:
                print("Computer not available. Try again")


    elif task == "exit":  
        print("\nExiting", end="")
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True) #ingen aning om vad det här betyder
        time.sleep(2)
        break
        
    else:
        print("Invalid input. Please enter 1, 2, 3, 4 or Exit")
        time.sleep(2)
        
        





