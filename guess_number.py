import random
import sys


def guess_number(name=""):
    player_wins = 0
    game_count = 0

    def guess_number_game():
        nonlocal name
        nonlocal player_wins

        playerChoice = input(
            f"\n{name} guess which number I'm thinking of... 1, 2, or 3.\n\n"
        )
        if playerChoice not in ["1", "2", "3"]:
            print(f"\n {name} please enter 1 , 2 or 3"),
            return guess_number_game()

        computerChoice = random.choice("123")

        print(f"{name} choice is {playerChoice}")
        print(f"My choice is {computerChoice}\n")

        player = int(playerChoice)

        computer = int(computerChoice)

        def number_decider(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name},you wins "
            else:
                return f"Sorry, {name}. better luck next time 😢"

        game_result = number_decider(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n game counts : {game_count}")
        print(f"\n players wins : {player_wins}")
        print(f"\n The winning percentage is : {player_wins / game_count:.1%}")

        print(f"\n Want to play again?")
        while True:
            playAgain = input(f"\nY for yes\nQ for quit\n \n")
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return guess_number_game()
        else:
            print(f"🎉🎉🎉🎉\n")
            print(f"\n Thank you for playing\n")
            if __name__ == "__main__":
                sys.exit(f"👋🏻 Bye {name}!")
            else:
                return

    return guess_number_game


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

    guess_my_number = guess_number(args.name)
    guess_my_number()
