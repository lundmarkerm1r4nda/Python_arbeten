# Välja ett tal

import random
number = random.randint(1,20)

numOfGuesses = 3
# Be om en siffra

while (numOfGuesses > 0):
    print ("Guess a number ")
    guess = int(input())
    print("You guessed ")
    print(guess)

    numOfGuesses -= 1
    # Kolla om siffran är större, mindre eller lika

    if (guess > number):
        print("You guessed too high. Try again.")

    elif (guess < number):
        print("You guessed too low. Try again.")

    else:
        print("Correct!")
        break

print("The number was ")
print (number)


# göra tre gånger

