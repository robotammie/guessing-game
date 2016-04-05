# Put your code here
import random
import sys

def play_game():
    print "I'm thinking of a number between 1 and 100."

    secret_number = random.randint(1, 100)
    print secret_number
    numbers_guessed = []
    global best_score

    while True:
        try:
            guess = int(raw_input("Enter your guess: "))
            # print numbers_guessed

            if guess < 1 or guess > 100:
                print "That is not a number between 1 and 100, try again."

            else:
                if guess in numbers_guessed:
                    print "You've guessed this number before."
                else:
                    numbers_guessed = numbers_guessed + [guess]


                if guess == secret_number:
                    score = len(numbers_guessed)
                    if best_score == None or score < best_score:
                        best_score = score
                    print "Congratulations, you guessed my number in %d tries!" % (score)
                    break
                elif guess > secret_number:
                    print "Your guess is too high, try again."
                else:
                    print "Your guess is too low, try again."

        except ValueError:
            print "Please try again with an integer between 1 and 100."

    play_again = raw_input("Would you like to play again? y/n ")
    if play_again == 'y' or play_again == 'yes':
        play_game()
    else:
        print "Thank you for playing! Your best score was %d!" % (best_score)
        sys.exit()



print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)
best_score = None
play_game()

