class Board:

    def __init__(self):
        self.table_cards = [] # lista pöydässä olevista korteista
        self.table_cards_gui = []

    def add_cards_to_board(self, kortit):
        for kortti in kortit:
            self.table_cards.append(kortti)

    def remove_card_from_table(self, kortti):
        self.table_cards.remove(kortti)

    def return_cards(self):
        return self.table_cards

    def return_gui_cards(self):
        return self.table_cards_gui

    def add_gui_card(self,kortti):
        self.table_cards_gui.append(kortti)

    def remove_gui_card(self, kortti):
        self.table_cards_gui.remove(kortti)

    def add_one_card_to_board(self,kortti):
        self.table_cards.append(kortti)

    def return_len_table_cards(self):
        return len(self.return_cards())

    def nollaa_table_cards(self):
        self.table_cards = []

    def nollaa_table_cards_gui(self):
        self.table_cards_gui = []