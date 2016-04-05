# Put your code here
import random

print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)
print "I'm thinking of a number between 1 and 100."

secret_number = random.randint(1, 100)
print secret_number

while True:
    guess = int(raw_input("Enter your guess: "))

    if guess == secret_number:
        print "Congratulations, you guessed it!"
        break

    elif guess > secret_number:
        print "Your guess is too high, try again."

    else:
        print "Your guess is too low, try again."