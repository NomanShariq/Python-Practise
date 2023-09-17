import sys
from guess_number import guess_number

from rps_game import rps


def play_game(name=""):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerChoice = input(
            "\n Please the value for which game you want to play?\n 1. Rock , Paper & Scissors.\n 2. Guess Number. \n x. want to exit ?\n"
        )

        if playerChoice.lower() not in ["1", "2", "x"]:
            print("\nPlease Enter The Following Value 1 , 2 ,x.")
            return play_game(name)
        welcome_back = True
        
        if playerChoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
            
        elif playerChoice == "2":
            guess_number_game = guess_number(name)
            guess_number_game()     
        
        else:
            print("🎉Thanks for playing !!")
            sys.exit(f" Bye {name}")
            

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Providing personalized choice game")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person who play game",
    )

    args = parser.parse_args()
    
    print(f"\n {args.name} Welcome to the Arcade")
    
    play_game(args.name)