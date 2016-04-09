# Put your code here
import random
import sys


# Introduction to guessing game
print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)

# Generates a random number between 1-100
secret_number = random.randint(1, 100)
print "I'm thinking of a number between 1 and 100."

# Creates variable to track best score
best_score = None

# List of guessed numbers
numbers_guessed = []

# play_game sta
play_game = True

# Continue playing game until condition reached (correct number guessed)
while play_game:

    # Determine if guess was not an integer
    guess = raw_input("Enter your guess: ")
    if not guess.isdigit():
        print "Please try again with an integer between 1 and 100."

    else:
        guess = int(guess)

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
               
                # Prompts to play game again or not    
                play_again = raw_input("Would you like to play again? y/n ")
                if play_again != 'y' and play_again != 'yes':
                    play_game = False
                else:
                    # clears out the guessed numbers cache
                    numbers_guessed = []
                    print "Let's play again! I'm thinking of a number between 1 and 100."
            
            # Determine if guess is too high or too low
            elif guess > secret_number:
                print "Your guess is too high, try again."
            else:
                print "Your guess is too low, try again."


print "Thank you for playing! Your best score was %d!" % (best_score)
exit()

