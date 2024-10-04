#Importing play_game function from PlayersLogic, which handles the game logic.
from PlayersLogic import play_game
from colorama import Fore, Style #Used to add color to the terminal output.
import sys #Used for exiting the program

def play_again(): #Infinite loop to keep asking the player if they want to play again.
    while True:
        print(" ") #Adds a space for better readability in the terminal.
        svar = input(Fore.GREEN + "PLAY AGAIN? (y/n) " + Style.RESET_ALL).lower()
        if svar == "y": #If players inputs "y", the game starts again.
            play_game()
        elif svar == "n": #If the player inputs "n", the game ends with a message and the program exits.
            print("See you again!")
            sys.exit()
        else: #If the player enters anything else and error message is displayed.
            print("Invalid input")

if __name__ == "__main__":
    play_game() #Starts the game.
    play_again() #After the game, it asks if the user wants to play again.