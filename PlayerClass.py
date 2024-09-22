from typing import List

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