import random

def initGame():
    print('')
    print("-----------------------------")
    print("Welcome to guess the number !")
    print("-----------------------------")
    print('')
    print("The number will be between 1 to 20")
    print('')


def mainGame():
    rNumber = random.randint(1, 20)
    userNumber = int(input("Choose a number : "))
    chance = 0
    
    while userNumber != rNumber:
        if chance != 5:
            userNumber = int(input("Choose a number : "))
            print("Try again !")
            chance += 1
            continue
        else:
            print('RIP you lose, the number was ' ,rNumber)
            break
    else:
        print('')
        print("Suiiiiiii !")
        print('You find the number, it was ',rNumber)


## Run function
def runProgram():
    initGame()
    mainGame()

## Start the game
runProgram()

