import random

#Rock,Paper,Scissors
def logo():
    print('///////////////////////////////////////////')
    print('///             ///             ///           ///')
    print('///             ///             ///    /////////')
    print('///       ////////     //////////           ///')
    print('///         //////     ////////////////    ///')
    print('///    //     ////     //////////           ///')
    print('///////////////////////////////////////////')
    print('RockPaperScissors by Jozef Komaromy')
    print('                 2017')
        

def main():
    
    def again():
        input()
        for i in range(0,3):
            print(' ')
        main()

    
            
    nums = ('(1)','(2)','(3)')
    choices = ('rock','paper','scissors')
    for i in range(0,3):
        print(nums[i] ,choices[i])
    print('Type a number between 1 and 3')

    #cChoice = choice of the pc
    cChoice = random.choice(choices)

    #take input
    try:
        choice = int(input('Choose:'))
        choice = choices[choice-1]
    except:
        again()

    print('You: ' + choice)
    print('Computer: ' + cChoice)

    def compare():
        def win():
            print('You win !!!!')
            again()
        def lose():
            print('You lose !!')
            again()
        def draw():
            print('Its a draw')
            again()
            
        if choice == cChoice:
            draw()
        elif choice == choices[0] and cChoice == choices[1]:
            lose()
        elif choice == choices[0] and cChoice == choices[2]:
            win()
        elif choice == choices[1] and cChoice == choices[2]:
            lose()
        elif choice == choices[1] and cChoice == choices[0]:
            win()
        elif choice == choices[2] and cChoice == choices[0]:
            lose()
        elif choice == choices[2] and cChoice == choices[1]:
            win()

    compare()

logo()
main()
    
    
