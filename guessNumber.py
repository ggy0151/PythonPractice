import random
guesstaken = 0

print('Hello! What is your name?')
Name=input()

print('Well, '+Name+', I am thinking of a number between 1 and 20.')
number=random.randint(1, 20)

while guesstaken < 6:
    print('Take a guess.')
    guess = input()
    guess =  int(guess)

    guesstaken = guesstaken+1

    if guess < number:
        print('Your guess is too low.')

    if guess > number :
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number :
        guesstaken= str(guesstaken)
        print('Good job, '+Name+'! You guessed my number in '+guesstaken+' guesses!')

if guess != number:
        number= str(number)
        print('Nope! The number I was thinking of was'+number)
