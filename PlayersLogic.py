from typing import List #Import List type hint for specifying list of integers.
from CardDeckClass import CardDeck #Import the CardDeck from CardDeckClass file.
from colorama import Fore, Style #Used to add color to the terminal output.
import AsciiArt #Importing the AsciiArt module to display logo art during the game.

class players:
    def __init__(self) -> None:
        #Initialize the players hand as an empty list and set the initial score to 0
        self.hand: List[int] = [] #List to store the players cards.
        self.score: int =0 #Start the score at 0

    def add_card(self, card: int) -> None: #Function that adds the card to players hand and updating the score.
        self.hand.append(card) #Add the drawn card to the hand list
        self.update_score() #After adding the card, update the score for player
    
    def update_score(self) -> None:
        #Calculate the total score of the cards in players hand
        total = 0 #Variable to track the totalt score.
        aces = 0 #Variable to count the number of aces in the hand.

        for card in self.hand:
            if card == 1: #If card is an ace value 1
                aces += 1 #Adding to aces
                total += 1
            else: #Otherwise, add the cards value to total
                total += card

        #Here we choose to let the program decide if its beneficial to count the ace without exceeding 21.
        while aces > 0 and total + 13 <= 21:
                total += 13 #Convert the ace value from 1 to 14.
                aces -= 1 #Decrease the amount of aces with one.

        #Update players score with the total.
        self.score = total
    
    def lost(self) -> bool: #Function checks if players exceeded 21
        return self.score > 21 #Return True if the score is over 21
    

def play_game() -> None: #Main function to play the game: initializes the deck, player and computer, and controls the game flow
    deck = CardDeck() #Create a new shuffled deck of cards
    player = players() #Create the player instance
    computer = players() #Create the computer instance

    print(AsciiArt.logo) #Display the game logo using ASCII art.
    print(Fore.BLUE + "\nPLAYERS TURN!" + Style.RESET_ALL) #Announce the players turn with colored text

    while True:
        card = deck.DrawCard() #Draw a card from the deck and save it in the variable card
        player.add_card(card) #Add the drawn card to players hand and update the score
        print(f"Card in hand: {card}. Total: {player.score}") #Display the current card and total score.

        if player.lost(): #Control if the player has lost by exceeding 21.
            print(Fore.RED + f"You got {player.score} and lost the game!" + Style.RESET_ALL)
            return #End the game if the player loses.
        
        while True:
            choice = input("Another card? (Y/N) ").lower() #Ask if the player wants to draw another card, converting the input to lowercase.
            if choice == "y" or choice == "n":
                break
            else:
                print(Fore.RED + "INVALID INPUT, please enter y or n" + Style.RESET_ALL)
        if choice != "y":
            break

    print(" ")
    print(Fore.YELLOW + "COMPUTERS TURN!" + Style.RESET_ALL) #Anounce the computers turn with colored text
    while computer.score < 16: #The computer will keep drawing cards until the score is near 16
        card = deck.DrawCard() #Draw a card for the computer and save it in variable card
        computer.add_card(card) #Add the card to computers hand and update the score
        print(f"Computers card: {card}. Total: {computer.score}") #Display the current card and total score.

        if computer.lost(): #Checking if the computer has lost by exceeding 21
            print(Fore.RED + f"Computer got {computer.score} and lost the game!" + Style.RESET_ALL)
            return #End the game if computer loses.

    print(Fore.MAGENTA + "\nRESULTS" + Style.RESET_ALL) #Display RESULTS in colored text.
    #Compare if the computer has lost by exceeding 21 or if the player has higher score than computer(Under 21).
    if computer.lost() or player.score > computer.score:
        print("Congrats player!")
    #Compare if the player has lost by exceeding 21 or if the computer has higher score than the player(Under 21).
    elif player.lost() or computer.score > player.score:
        print("Computer wins, you Loose!")
    else: 
        print("Draw!") #Its a draw if both the player and the computer have the same score.