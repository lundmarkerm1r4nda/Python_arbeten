import random

def mathtergame ():
    x_number = random.randint(1,10)
    y_number = random.randint(1,10)
    num_of_guesses = 1
    equation_answer = x_number
    points = 0
    
    print(f"\nX * {y_number} =", x_number*y_number)
    print("What is X\n")

    while num_of_guesses > 0:
        try:
            useranswer = int(input("Your answer: "))

            num_of_guesses -= 1

            if useranswer == equation_answer:
                points += 1
                print("Rätt")
                print (f"+1 Point, you have {points} point(s)")
                

            elif useranswer > equation_answer:
                print(f"\nFör högt, {useranswer} * {y_number} =", useranswer*y_number)
                

            else:
                print(f"\nFör lågt, {useranswer} * {y_number} =", useranswer*y_number)
                

        except ValueError:
            print("\nSkriv in ett nummer\n")

mathtergame()