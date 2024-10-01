from typing import List
from CardDeckClass import CardDeck 
from colorama import Fore, Style

class players:
    def __init__(self) -> None:
        #Create the players hand and set the initial score to 0
        self.hand: List[int] = [] #Players cards
        self.score: int =0 #Start the score with 0

    def add_card(self, card: int) -> None:
        self.hand.append(card) #Add the card to the hand list
        self.update_score() #After adding the card, update the score for player
    
    def update_score(self) -> None:
        #Calculate the total score of the cards in players hand
        total = 0 #Keep track of totalt score
        aces = 0 #Keeps tack of aces in hand
        for card in self.hand:
            if card == 1: #If card is an ace
                aces += 1 #Add to aces
                total += 1
            else: #Otherwise, add the cards value to total
                total += card

        #Here i choose to let the program decide if its beneficial to count the ace or not
        while aces > 0 and total + 13 <= 21:
                total += 13 #Count the ace as 14
                aces -= 1 #Decrease the amount of aces with one
        #Update players score with the total
        self.score = total
    
    def lost(self) -> bool: #Return true if players score exceeds 21
        return self.score > 21
    

def play_game() -> None: #Create deck and the player/computer
    deck = CardDeck()
    player = players()
    computer = players()
    print(Fore.BLUE + "\nPLAYERS TURN!" + Style.RESET_ALL)
    while True:
        card = deck.DrawCard() #Draw a card from the deck and save it in card
        player.add_card(card) #Add the card to players hand and update the score
        print(f"Card in hand: {card}. Total: {player.score}")

        if player.lost(): #Control if the player has lost above
            print(Fore.RED + f"You got {player.score} and lost the game!" + Style.RESET_ALL)
            return
        
        choice = input("Another card? (Y/N)").lower() #Ask if the player wants to draw another card
        if choice != "y": #If not, break the loop
            break
    print(" ")
    print(Fore.YELLOW + "COMPUTERS TURN!" + Style.RESET_ALL)
    while computer.score < 17: #The computer will keep drawing cards until the score is near 18
        card = deck.DrawCard() #Draw a card for the computer
        computer.add_card(card) #Add the card to computers hand and update the score
        print(f"Computers card: {card}. Total: {computer.score}")

        if computer.lost(): #Checking if the computer has lost above
            print(Fore.RED + f"Computer got {computer.score} and lost the game!" + Style.RESET_ALL)
            return
    #Compare the results to choose the winner.
    print(Fore.MAGENTA + "\nRESULTS" + Style.RESET_ALL)
    if computer.lost() or player.score > computer.score:
        print("Congrats player!") #Player wins if the computer loose or has higher score than computer(Under 21)
    elif player.lost() or computer.score > player.score: #Computer wins if the player loose or has higher score than player
        print("Computer wins, you Loose!")
    else: 
        print("Draw!") #For draw situations