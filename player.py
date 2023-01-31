from card import Card
from PyQt5.QtWidgets import QLabel

class Player:

    def __init__(self, name):
        self.name = name
        self.player_hand = []
        self.player_gui_hand = []
        self.player_collected_cards = 0
        self.score = 0
        self.cottages = 0
        self.padat = 0
        self.assat = 0
        self.ruutu_10 = 0
        self.pata_2 = 0
        self.alku_kasi_luotu = False
        self.vuoro_pelattu = False
        self.onko_nostanut_poydasta = 0

    def get_name(self):
        return self.name

    def get_player_hand(self):
        return self.player_hand

    def get_player_gui_cards(self):
        return self.player_gui_hand

    def get_player_score(self):
        return self.score

    def uptate_score(self,points):
        self.score += points

    def return_cottages(self):
        return self.cottages

    def add_cottage(self):
        self.cottages += 1

    def add_cards_to_hand(self, kortit):
        for kortti in kortit:
            self.player_hand.append(kortti)

    def remove_card_from_hand(self,kortti):
        self.player_hand.remove(kortti)

    def add_gui_card(self, kortti):
        self.player_gui_hand.append(kortti)

    def remove_gui_card(self, kortti):
        self.player_gui_hand.remove(kortti)

    def add_one_card_to_hand(self, kortti):
        self.player_hand.append(kortti)

    def onko_alku_kasi_luotu(self):
        return self.alku_kasi_luotu

    def muuta_alku_kasi(self):
        self.alku_kasi_luotu = True

    def alku_kasi_ei_luotu(self):
        self.alku_kasi_luotu = False

    def onko_vuoro_pelattu(self):
        return self.vuoro_pelattu

    def muuta_vuoro_pelattu(self):
        if self.onko_vuoro_pelattu() == False:
            self.vuoro_pelattu = True
        elif self.onko_vuoro_pelattu() == True:
            self.vuoro_pelattu = False

    def get_player_collected_cards(self):
        return self.player_collected_cards

    def collect_card(self):
        self.player_collected_cards += 1

    def collect_multiple_cards(self, amount):
        self.player_collected_cards += amount

    def return_padat(self):
        return self.padat

    def lisaa_pata(self):
        self.padat += 1

    def return_assat(self):
        return self.assat

    def lisaa_assa(self):
        self.assat += 1

    def set_keratut_kortit(self, amount):
        self.player_collected_cards = amount

    def set_score(self, amount):
        self.score = amount

    def set_cottages(self, amount):
        self.cottages = amount

    def set_padat(self, amount):
        self.padat = amount

    def set_assat(self, amount):
        self.assat = amount

    def set_onko_vuoro_pelattu(self, boolean):
        if boolean == 'False':
            self.vuoro_pelattu = False
        elif boolean == 'True':
            self.vuoro_pelattu = True

    def return_ruutu_10(self):
        return self.ruutu_10

    def lisaa_ruutu_10(self):
        self.ruutu_10 += 1

    def return_pata_2(self):
        return self.pata_2

    def lisaa_pata_2(self):
        self.pata_2 += 1

    def set_ruutu_10(self, amount):
        self.ruutu_10 = amount

    def set_pata_2(self, amount):
        self.pata_2 = amount

    def nostaa_poydasta(self):
        self.onko_nostanut_poydasta = 1

    def nollaa_nostanut_poydasta(self):
        self.onko_nostanut_poydasta = 0

    def return_nostaa_poydasta(self):
        return self.onko_nostanut_poydasta

    def set_nostaa_poydasta(self, amount):
        self.onko_nostanut_poydasta = amount





