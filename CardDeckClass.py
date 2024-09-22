import random

class CardDeck:
    def __init__(self) -> None:
        self.cards = list(range(1,14)) * 4 #Creating a card deck with the values 1-13, colors does not matter but i multiply it by 4 to get a realistic card deck.
        random.shuffle(self.cards) #Mix the card deck with the shuffle method
        
    def DrawCard(self) -> int:
        return self.cards.pop() #Remove and return the last card from deck