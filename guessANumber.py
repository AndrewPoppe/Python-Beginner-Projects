import random
# Number guessing game
def main():
    def firstTime():
        print('Welcome')
        print('Guess a number between 1 and 100')
        print('You have 10 guesses')
        fMain()

    def fMain():
        guesses = 0;
        found = False;
        randomNum = random.randint(1, 100);
        while guesses < 10:
            while not found:
                try:
                    userGuess = int(input('Your Guess:'))
                    guesses += 1
                    if userGuess == randomNum:
                        print('You got it!!');
                        found = True;
                        again()
                    elif userGuess < randomNum:
                        print('Guess Higher');
                    elif userGuess > randomNum:
                        print('Guess Lower');
                    else:
                        print('Type a number between 1 and 100')
                        fMain()
                    if guesses >= 10:
                        print('You used all your guesses. You LOSE!!')
                        again()

                except:
                    print('Type a number between 1 and 100')
                    exit()

    def again():
        print('Do you want to play again ?')
        pAgain = input('y/n:')
        if pAgain == 'y':
            for i in range(0,6):
                print(' ')
            fMain();
        elif pAgain == 'n':
            exit()
        else:
            again()

    firstTime()



main()
    


