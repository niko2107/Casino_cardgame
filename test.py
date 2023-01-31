import unittest
from game import Game
from player import Player
from card import Card
from deck import Deck

class Test(unittest.TestCase):

    def test_create_player(self):
        pelaaja = Player("Janne")
        pelaajan_nimi = pelaaja.get_name()
        self.assertEqual('Janne', pelaajan_nimi)

    def test_create_deck(self):
        pakka = Deck()
        pakka.create_deck()
        pakka.shuffle_deck()
        pakan_kortti_lkm = pakka.cards_left()
        self.assertEqual(52, pakan_kortti_lkm)

    def test_deal_cards_to_players(self):
        pakka = Deck()
        pakka.create_deck()
        pakka.shuffle_deck()
        pelaaja = Player('Mikko')
        jaettavat_kortit = pakka.deal(4)
        pelaaja.add_cards_to_hand(jaettavat_kortit)
        pelaajan_kortit = pelaaja.get_player_hand()
        self.assertEqual(4, len(pelaajan_kortit))

    def test_player_collect_10_of_diamonds(self):
        kortti = Card('D', 10)
        pelaaja = Player('Juho')
        if kortti.get_card_suit() == 'D' and kortti.get_card_value() == 10:
            pelaaja.lisaa_ruutu_10()
        self.assertEqual(1, pelaaja.return_ruutu_10())

    def test_peli_vuorot(self):
        pelaaja_1 = Player('Matias')
        pelaaja_2 = Player('Sanni')
        peli = Game()
        peli.add_player(pelaaja_1)
        peli.add_player(pelaaja_2)
        self.assertEqual(2, peli.count_players())
        self.assertEqual(0, peli.get_player_turn())
        peli.next_player_turn()
        self.assertEqual(1, peli.get_player_turn())
        self.assertEqual(False, pelaaja_1.onko_vuoro_pelattu())
        pelaaja_1.muuta_vuoro_pelattu()
        self.assertEqual(True, pelaaja_1.onko_vuoro_pelattu())

    def test_remove_card_from_hand(self):
        card_1 = Card('D', 3)
        card_2 = Card('S', 5)
        card_3 = Card('H', 10)

        pelaaja = Player('Patrick')
        pelaaja.add_one_card_to_hand(card_1)
        pelaaja.add_one_card_to_hand(card_2)
        pelaaja.add_one_card_to_hand(card_3)
        pelaajan_kortit = pelaaja.get_player_hand()
        self.assertEqual(3, len(pelaajan_kortit))
        pelaaja.remove_card_from_hand(card_3)
        self.assertEqual(2, len(pelaajan_kortit))

    def test_change_card_value(self):
        card = Card('H', 7)
        self.assertEqual('H', card.get_card_suit())
        self.assertEqual(7, card.get_card_value())
        card.change_card_value(3)
        self.assertEqual(3, card.get_card_value())

if __name__ == "__main__":
    unittest.main()


