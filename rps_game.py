from enum import Enum
import random
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerChoice = input("Enter Your Value\n 1. Rock \n 2. Paper \n 3.Scissors\n\n")
player = int(playerChoice)

if player > 1 | player < 3 :
    sys.exit("Please Enter the 1 , 2 , 3")
    
computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("Player choice is " + str(RPS(player)).replace("RPS.","") + ".")
print("Player choice is " + str(RPS(computer)).replace("RPS.","") + ".")
print("")

if player == 1 and computer == 3:
    print("Player Wins!!")
elif player == 2 and computer == 1:
    print("Player Wins!!")
elif player == 3 and computer == 2:
    print("Player Wins!!")
elif player ==  computer:
    print(" Tie!! ")
else :
    print("Python Wins !!")
    
