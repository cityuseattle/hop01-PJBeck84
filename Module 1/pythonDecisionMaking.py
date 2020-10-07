name = input('Please enter your name: ')
guess = int(input('Please guess an integer between 1 and 6: '))
randomNumber = 5

if (guess == randomNumber):
    print('\nCongrats, you got it!')
else:
    print('\nOops, better luck next time!')

print('\nHow old are you?')
age = int(input())

if age < 21:
    print('You are too young to have a drink.')
elif age >= 80:
    print('Ok, you will get a free drink.')
else:
    print('Sure, enjoy your drink.')