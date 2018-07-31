import random

TIE = 0
COMPUTER_WINS = 1
PLAYER_WINS = 2

ROCK = 1
PAPER = 2
SCISSORS = 3

def main(): #void function
    CONTINUE = "Y"
    while CONTINUE == "Y":
        PLAYER_SELECTION = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        COMPUTER_SELECTION = random.randint(1,3)
        print("Computer selects ", Choice(COMPUTER_SELECTION))
        print("Player selects ", Choice(PLAYER_SELECTION))

        RESULT_OF_THE_GAME = RockPaperScissors(COMPUTER_SELECTION,PLAYER_SELECTION)

        if RESULT_OF_THE_GAME == TIE:
            print("It was a Tie!!\n")
        elif RESULT_OF_THE_GAME == COMPUTER_WINS:
            print("Computer wins!!\n")
        else:
            print("Player wins!!\n")
            
        CONTINUE = input("Would you like to play again? Y for yes: ")

def RockPaperScissors(COMPUTER,PLAYER):
    if COMPUTER == PLAYER:
        return TIE
    
    if COMPUTER == ROCK:
        if PLAYER == SCISSORS:
            return COMPUTER_WINS
        elif PLAYER == PAPER:
            return PLAYER_WINS
        else:
            return "Something went wrong"
        
    if COMPUTER == PAPER:
        if PLAYER == ROCK:
            return COMPUTER_WINS
        elif PLAYER == SCISSORS:
            return PLAYER_WINS
        else:
            return "Something went wrong"
        
    if COMPUTER == SCISSORS:
        if PLAYER == ROCK:
            return PLAYER_WINS
        elif PLAYER == PAPER:
            return COMPUTER_WINS
        else:
            return "Something went wrong"
        
    #elif COMPUTER == ROCK and PLAYER == SCISSORS:
    #    return COMPUTER_WINS
    #elif COMPUTER == PAPER and PLAYER == ROCK:
    #    return COMPUTER_WINS
    #elif COMPUTER == SCISSORS and PLAYER == PAPER:
    #    return COMPUTER_WINS
    #else:
    #   return PLAYER_WINS  

def Choice(SELECTION): #change our numerical selection into a string (1 will be Rock)
    if SELECTION == ROCK:
        return "Rock"
    elif SELECTION == PAPER:
        return "Paper"
    elif SELECTION == SCISSORS:
        return "Scissors"
    else:
        return "Selection is invalid"

main()
