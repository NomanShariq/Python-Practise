from enum import Enum
import random
import sys

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        
        nonlocal player_wins
        nonlocal python_wins
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
        # print("Your choice" +" "+ playerChoice + ".")
        # print("Python choice"+" " + computerChoice + ".")
        print("Player choice is " + str(RPS(player)).replace("RPS.","") + ".")
        print("Python choice is " + str(RPS(computer)).replace("RPS.","") + ".")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins 
            nonlocal python_wins 
            
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You Wins!!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return " 🎉 You Wins!!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return " 🎉 You Wins!!"
            elif player ==  computer:
                return " 😲 Tie!! "
            else :
                python_wins += 1
                return " 🐍 Python Wins !!"

        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print("\n Game Count:" + str(game_count))
        print("\n Player Wins:" + str(player_wins))
        print("\n Python Wins:" + str(python_wins))
            
        print("\nPlay Again?")
        while True:    
            Playagain = input("\nY for Yes \nQ for Quit\n\n")
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
    
    return play_rps
    
play = rps()

play()