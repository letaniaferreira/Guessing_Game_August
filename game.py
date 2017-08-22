"""A number-guessing game."""
import random

print 'Hello there! What is your name?'
name = raw_input('Name: ')

number = random.randint(1, 100)

num_guesses = 0

while True:

    guess = int(raw_input('Pick a number between 1 and 100: '))
    num_guesses += 1
    if guess > number:
        print 'Too high!'
    elif guess < number:
        print 'Too low!'
    else:
        print 'Great job, {}! You found my number in {} guesses'.format(name, num_guesses)
        break
