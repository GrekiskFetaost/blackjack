#Importing CardDeck and Players from the classes
from PlayersLogic import play_game
from colorama import Fore, Style
import sys

def play_again():
    while True:
        print(" ")
        svar = input(Fore.GREEN + "PLAY AGAIN? (y/n)" + Style.RESET_ALL).lower()
        if svar == "y":
            play_game()
        elif svar == "n":
            print("See you again!")
            sys.exit()
        else:
            print("Invalid input")

if __name__ == "__main__":
    play_game()
    play_again()