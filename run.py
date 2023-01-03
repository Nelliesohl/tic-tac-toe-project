# https://docs.python.org/3/library/os.html
import os
# https://github.com/timofurrer/colorful
import colorful


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
            print("Let's play!")
            break
        else:
            print("\nIncorrect input. Try again:")


game_introduction()
start_game()
