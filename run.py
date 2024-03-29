# https://docs.python.org/3/library/os.html
import os
# https://docs.python.org/3/library/random.html
import random
# https://github.com/timofurrer/colorful
import colorful

# Global variables
grid = [str("-") for i in range(1, 10)]
current_player = "x"
winner = None


def game_introduction():
    """
    Prints the initializing game introduction to console when script runs.
    """
    print("\n" + " " * 13 + "TIC - TAC - TOE")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("=========================================\n")
    print("Welcome Player: " + colorful.bold_green('x') + "\n")
    print("You will go up against the computer in a")
    print("classical game of Tic-Tac-Toe.\n")
    print("The player who succeeds in placing three")
    print("of their marks in a horizontal, vertical,")
    print("or diagonal row is the winner.\n")
    print("If played optimally by both players,")
    print("the game always ends in a tie.\n")
    print("=========================================\n")


def start_game():
    """
    Prompts user input to start game.
    Prints error message if user input is incorrect.
    """
    while True:
        start = input("Press 's' followed by 'enter' to start!\n").lower()

        if start == 's':
            break
        else:
            print("\nIncorrect input. Try again:")


# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear_console():
    """
    Clears console to simplify UX and clear visual clutter
    when function is called.
    """
    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums

    if os.name == "posix":
        # for OS => Unix / Linux / MacOS / BSD / etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        #  for OS => DOS / Windows
        os.system('CLS')


def print_game_board():
    """
    Prints game board and reference board to console when function is called.
    """
    print("\n" + " " * 13 + "TIC - TAC - TOE")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("=========================================\n")
    print("  " + "-------------" + " " * 11 + "-------------")
    print("  | " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |" +
          " " * 9 + "  | " + "1" + " | " + "2" + " | " + "3" + " |")
    print("  " + "|---|---|---|" + " " * 11 + "|---|---|---|")
    print("  | " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |" +
          " " * 9 + "  | " + "4" + " | " + "5" + " | " + "6" + " |")
    print("  " + "|---|---|---|" + " " * 11 + "|---|---|---|")
    print("  | " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |" +
          " " * 9 + "  | " + "7" + " | " + "8" + " | " + "9" + " |")
    print("  " + "-------------" + " " * 11 + "-------------\n")
    print("=========================================")
    print("Player: " + colorful.bold_green('x') + " | Computer: " +
          colorful.bold_red('o') + " | Reference Board \n")


def get_user_move():
    """
    Prompts user to input a number between 1-9 to place their mark.
    Checks if user input and grid choice is valid.
    Displays error message if input is invalid.
    """
    while True:
        user = input("[1-9]... What will be your choice ?\n")

        if user in [str(i) for i in range(1, 10)] and grid[int(user)-1] == "-":
            grid[int(user)-1] = colorful.bold_green(current_player)
            break
        else:
            print("\nInvalid input. Try again:")


def get_computer_move():
    """
    Generates a random number between 0-8.
    Checks if random generated computer choice is available in grid.
    Generates a new number if spot is taken.
    Updates grid with computer move.
    """
    while True:
        computer_choice = random.randint(0, 8)

        if current_player == "o" and grid[computer_choice] == "-":
            grid[computer_choice] = colorful.bold_red('o')
            break


def alternate_player():
    """
    Alternates between player and computer
    """
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"


def check_horizontal(grid):
    """
    Checks horizontal rows for 3 identical marks to see if there's a winner.
    """
    if grid[0] == grid[1] == grid[2] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[3] == grid[4] == grid[5] and grid[3] != "-":
        winner = grid[3]
        return True
    elif grid[6] == grid[7] == grid[8] and grid[6] != "-":
        winner = grid[6]
        return True


def check_vertical(grid):
    """
    Checks vertical rows for 3 identical marks to see if there's a winner.
    """
    if grid[0] == grid[3] == grid[6] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[1] == grid[4] == grid[7] and grid[1] != "-":
        winner = grid[1]
        return True
    elif grid[2] == grid[5] == grid[8] and grid[2] != "-":
        winner = grid[3]
        return True


def check_diagonal(grid):
    """
    Checks diagonal rows for 3 identical marks to see if there's a winner.
    """
    if grid[0] == grid[4] == grid[8] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[2] == grid[4] == grid[6] and grid[4] != "-":
        winner = grid[2]
        return True


def check_board_for_win(grid):
    """
    Checks horizontal, vertical and diagonal rows for winner.
    Prints feedback if winner is found.
    """

    if check_horizontal(grid) or check_vertical(grid) or check_diagonal(grid):
        if winner == "x":
            print(f"\nCongratulations {winner} !\n")
            print("You're on your way to becoming a Tic-Tac-Toe Champion.\n")
        else:
            print("\nOhno.. The computer won!\n")


def check_board_for_tie(grid):
    """
    Checks grid for tie
    Prints feedback if board is full and no winner has been found.
    """
    if "-" not in grid:
        print("\nIt is a tie!\n")


def play_again():
    """
    Prompts user if they want to play again
    """
    while True:
        play_again = input(
        "Would you like to practice some more? [yes/no]\n").lower()

        if play_again == "yes":
            clear_console()
            clear_board()
            main()
        elif play_again == "no":
            clear_console()
            print("\nThank you for playing! Come back to practice soon")
        else: 
            print("\nInvalid input. Try again:")


def clear_board():
    """
    Resets grid list
    """
    global grid
    grid = [str("-") for i in range(1, 10)]


game_introduction()
start_game()
clear_console()
print_game_board()
get_user_move()
clear_console()
print_game_board()
