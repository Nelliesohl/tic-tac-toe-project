# https://docs.python.org/3/library/os.html
import os
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


game_introduction()
start_game()
clear_console()
print_game_board()
get_user_move()
clear_console()
print_game_board()
