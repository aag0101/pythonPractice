import random

guesstaken = 0

print('Hello! What is your name?')

myName = input()

number = random.randint(1,20)

print('Well,' + myName + ', I am thinking of a number bwtween 1 and 20')

for guesstaken in range(6):
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('your guess is low')

    if guess > number:
        print('your guess is high')

    if guess == number:
        break

if guess == number:
    guesstaken = str(guesstaken + 1)
    print('good job,' + myName + 'number ' + guesstaken + 'Guess')

if guess!=number:
    number = str(number)
    print('Nope  correct number is ' + number + '.')


            
        
      
