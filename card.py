class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        # diamonds (D) = ruutu, clubs (C) = risti, hearts (H) = hertta, spades (S) = pata

    def get_card_suit(self):
        return self.suit

    def get_card_value(self):
        return self.value

    def change_card_value(self,new_val):
        self.value = new_val


