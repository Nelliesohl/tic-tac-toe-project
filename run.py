""" https://github.com/timofurrer/colorful """
import colorful


def game_introduction():
    """
    Prints game introduction to console when script runs.
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


game_introduction()
