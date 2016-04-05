# Put your code here
import random

print "Hello, welcome to the Guessing Game!"
name = raw_input("What is your name? ")
print "Hello, %s!" % (name)
print "I'm thinking of a number between 1 and 100."

secret_number = random.randint(1, 100)
print secret_number