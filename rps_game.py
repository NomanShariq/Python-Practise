from enum import Enum
import random
import sys

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
                
    playerChoice = input("Enter Your Value\n 1. Rock \n 2. Paper \n 3.Scissors\n\n")
    if playerChoice not in ["1","2","3"]:
        print("Please Enter the 1 , 2 , 3. ")
        return 
    player = int(playerChoice)
            
    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print("")
    print("Your choice" +" "+ playerChoice + ".")
    print("Python choice"+" " + computerChoice + ".")
    # print("Player choice is " + str(RPS(player)).replace("RPS.","") + ".")
    # print("Python choice is " + str(RPS(computer)).replace("RPS.","") + ".")
    print("")

    if player == 1 and computer == 3:
        print(" 🎉 You Wins!!")
    elif player == 2 and computer == 1:
        print(" 🎉 You Wins!!")
    elif player == 3 and computer == 2:
        print(" 🎉 You Wins!!")
    elif player ==  computer:
        print(" 😲 Tie!! ")
    else :
        print(" 🐍 Python Wins !!")

    print("Play Again?")
    while True:    
        Playagain = input("\nY for Yes \nQ for Quit\n")
        if Playagain not in ['y','q']:
            continue
        else:
            break
        
    if Playagain.lower() == "y":
        return play_rps()
    else : 
        print("\n🎉🎉🎉🎉")
        print('Thank you playing\n')
        sys.exit("👋🏻Bye")        

play_rps()