from enum import Enum
import random
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
Playagain = True
    
while Playagain:
    
        playerChoice = input("Enter Your Value\n 1. Rock \n 2. Paper \n 3.Scissors\n\n")
        player = int(playerChoice)

        if player > 1 | player < 3 :
            sys.exit("Please Enter the 1 , 2 , 3")
            
        computerChoice = random.choice("123")
        computer = int(computerChoice)

        print("")
        print("You choice" +" "+ playerChoice + ".")
        print("Python choice"+" " + computerChoice + ".")
        # print("Player choice is " + str(RPS(player)).replace("RPS.","") + ".")
        # print("Python choice is " + str(RPS(computer)).replace("RPS.","") + ".")
        print("")

        if player == 1 and computer == 3:
            print(" 🎉 Player Wins!!")
        elif player == 2 and computer == 1:
            print(" 🎉 Player Wins!!")
        elif player == 3 and computer == 2:
            print(" 🎉 Player Wins!!")
        elif player ==  computer:
            print(" 😲 Tie!! ")
        else :
            print(" 🐍 Python Wins !!")

        Playagain = input("\nPlay Again?\n Y for Yes \n Q for Quit\n\n")
        
        if Playagain.lower() == "y":
            continue
        else : print("\n🎉🎉🎉🎉")
        print('Thank you playing\n')
        Playagain = False
        
sys.exit("👋🏼 Bye")