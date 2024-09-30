# Välja ett tal

correctNumber = 6
numOfGuesses = 3
# Be om en siffra

while (numOfGuesses > 0):
    print ("Guess a number ")
    guess = int(input())
    print("You guessed ")
    print(guess)

    numOfGuesses -= 1
    # Kolla om siffran är större, mindre eller lika

    if (guess > correctNumber):
        print("You guessed too high. Try again.")

    elif (guess < correctNumber):
        print("You guessed too low. Try again.")

    else:
        print("Correct!")
        break



# göra tre gånger

