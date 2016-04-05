# Put your code here
import random

print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)
print "I'm thinking of a number between 1 and 100."

secret_number = random.randint(1, 100)
print secret_number
numbers_guessed = []

while True:
    guess = int(raw_input("Enter your guess: "))
    numbers_guessed = numbers_guessed + [guess]
    # print numbers_guessed

    if guess == secret_number:
        print "Congratulations, you guessed it the number in %d tries!" % (len(numbers_guessed))
        break

    elif guess > secret_number:
        print "Your guess is too high, try again."

    else:
        print "Your guess is too low, try again."