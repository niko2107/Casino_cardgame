from random import shuffle
from card import Card

class Deck:

    def __init__(self):
        self.deck_cards = []

    # diamonds (D) = ruutu, clubs (C) = risti, hearts (H) = hertta, spades (S) = pata

    def create_deck(self):
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        suits = ['D', 'C', 'H', 'S']

        for suit in suits:
            for val in values:
                kortti = Card(suit, val)
                self.deck_cards.append(kortti)

    def shuffle_deck(self):
        shuffle(self.deck_cards)

    def deal(self, amount):
        jaettavat_kortit = []
        for i in range(amount):
            if self.cards_left() == 0:
                break
            jaettavat_kortit.append(self.deck_cards.pop())
        return jaettavat_kortit

    def cards_left(self):
        return len(self.deck_cards)

    def return_deck(self):
        return self.deck_cards

    def add_card_to_deck(self, kortti):
        self.deck_cards.append(kortti)