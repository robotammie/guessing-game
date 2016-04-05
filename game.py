# Put your code here
import random
import sys

def play_game():
    print "I'm thinking of a number between 1 and 100."

    # Generates a random number between 1-100
    secret_number = random.randint(1, 100)
    # print secret_number

    # List of guessed numbers
    numbers_guessed = []

    # References to best_score variable outside of function so no local variable error
    global best_score

    # Continue playing game until condition reached (correct number guessed)
    while True:

        # Determine if guess was not an integer
        try:
            guess = int(raw_input("Enter your guess: "))
        except ValueError:
            print "Please try again with an integer between 1 and 100."

        # Determine if guess was out of bounds
        if guess < 1 or guess > 100:
            print "That is not a number between 1 and 100, try again."

        else:
            # Determine if number was already guessed
            if guess in numbers_guessed:
                print "You've guessed this number before."
            # Adds guess to list of guessed numbers
            else:
                numbers_guessed = numbers_guessed + [guess]

            # Determine if guess is correct
            if guess == secret_number:
                # Determine score and update best score if necessary
                score = len(numbers_guessed)
                if best_score == None or score < best_score:
                    best_score = score
                print "Congratulations, you guessed my number in %d tries!" % (score)
                # Ends round of game
                break
            # Determine if guess is too high or too low
            elif guess > secret_number:
                print "Your guess is too high, try again."
            else:
                print "Your guess is too low, try again."

    # Prompts to play game again or not    
    play_again = raw_input("Would you like to play again? y/n ")
    if play_again == 'y' or play_again == 'yes':
        play_game()
    else:
        print "Thank you for playing! Your best score was %d!" % (best_score)
        # Exits game
        sys.exit()


# Introduction to guessing game
print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)

# Creates variable to track best score
best_score = None

# Starts the game
play_game()

