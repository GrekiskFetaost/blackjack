#Importing CardDeck and Players from the classes
from CardDeckClass import CardDeck 
from PlayerClass import players
import sys

def play_game() -> None: #Create deck and the player/computer
    deck = CardDeck()
    player = players()
    computer = players()

    print("Players turn!")
    while True:
        card = deck.DrawCard() #Draw a card from the deck and save it in card
        player.add_card(card) #Add the card to players hand and update the score
        print(f"Kortet i handen: {card}. Du har totalt: {player.score}")

        if player.lost(): #Control if the player has lost above
            print(f"Du fick {player.score} och förlorade spelet!")
            return
        
        choice = input("Vill du dra ett till kort? (J/N): ").lower() #Ask if the player wants to draw another card
        if choice != "j": #If not, break the loop
            break

    print("Computers turn!")
    while computer.score < 18: #The computer will keep drawing cards until the score is near 18
        card = deck.DrawCard() #Draw a card for the computer
        computer.add_card(card) #Add the card to computers hand and update the score
        print(f"Computers card: {card}. Computer har totalt: {computer.score}")

        if computer.lost(): #Checking if the computer has lost above
            print(f"Datorn fick {computer.score} och förlorade spelet!")
            return
    #Compare the results to choose the winner.
    if computer.lost() or player.score > computer.score:
        print("Congrats player!") #Player wins if the computer loose or has higher score than computer(Under 21)
    elif player.lost() or computer.score > player.score: #Computer wins if the player loose or has higher score than player
        print("Computer wins, you Loose!")
    else: 
        print("Draw! ") #For draw situations
    
def play_again():
    while True:
        svar = input("Play again? (j/n)").lower()
        if svar == "j":
            play_game()
        elif svar == "n":
            print("See you again!")
            sys.exit()
        else:
            print("Invalid input")


if __name__ == "__main__":
    play_game()
    play_again()