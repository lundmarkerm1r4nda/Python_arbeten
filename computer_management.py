#Behövs: Arrays, Len(), count, while, for, it
#wat do you wanna do, add, or send pc

computers = ["2020","2021","2022","2023"]
on_service_computers = ["2017","2018","2019"]


while True:
    print(f"Available computers: {computers}\n")
    to_service_computers = input("What computer is going to Service?\n")
    computers.remove(to_service_computers)
    on_service_computers.append(to_service_computers)
    print(f"Computers on Service: {on_service_computers}")
    print(f"Available Computers: {computers}")

    break

