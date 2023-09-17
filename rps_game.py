from enum import Enum
import random
import sys

def rps(name=""):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
                    
        playerChoice = input(f"\n{name} , enter Your Value.....\n 1. Rock \n 2. Paper \n 3.Scissors\n\n")
        if playerChoice not in ["1","2","3"]:
            print(f"{name} , please Enter the 1 , 2 , 3. \n")
            return play_rps()
        
        player = int(playerChoice)
                
        computerChoice = random.choice("123")
        computer = int(computerChoice)

        print("")
        print(f"\n{name} choice is {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"\nPython choice is {str(RPS(computer)).replace('RPS.','').title()}.")
        print("")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins 
            nonlocal python_wins 
            
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name} You Wins!!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name} You Wins!!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name} You Wins!!"
            elif player ==  computer:
                return " 😲 Tie!! "
            else :
                python_wins += 1
                return f" 🐍 Python Wins !!, sorry {name} 😢 \n"

        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\n Game Count: {game_count}.")
        print(f"\n {name}'s Wins: {player_wins}.")
        print(f"\n Python Wins: {python_wins}.")
            
        print(f"\nPlay Again? {name}")
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
            if __name__ == "__main__":
                sys.exit(f"👋🏻 Bye {name}!")
            else:
                return       
    
    return play_rps
    
rock_paper_scissors = rps()

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description = "Providing personalized choice"
    )

    parser.add_argument(
        "-n" , "--name" , metavar='name',
        required=True , help="please enter given number.."
    )
    
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()