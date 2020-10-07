attempts = 0
randomNumber = 5

while attempts <= 2:
    guess = int(input('Please guess an integer between 1 and 6: '))

    if (int(guess) == randomNumber):
        print('\nCongrats, you got it!')
    else:
        print('\nOops, better luck next time!')

    attempts += 1