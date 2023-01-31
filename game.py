from player import Player
from deck import Deck
from board import Board

class Game:

    def __init__(self):
        self.players_list = []
        self.player_turn_vrbl = 0
        self.kierros_jarjestus = 1

    def add_player(self, pelaaja):
        self.players_list.append(pelaaja)

    def get_players(self):
        return self.players_list

    def get_player_turn(self):
        if self.player_turn_vrbl >= len(self.get_players()):
            self.player_turn_vrbl = 0
        return int(self.player_turn_vrbl)

    def next_player_turn(self):
        self.player_turn_vrbl += 1

    def count_player_points(self, player):
        return player.get_player_score()

    def count_players(self):
        return len(self.players_list)

    def set_player_turn(self, new_turn):
        self.player_turn_vrbl = new_turn

    def get_kierros_jarjestus(self):
        return self.kierros_jarjestus

    def add_kierros_jarjestus(self):
        self.kierros_jarjestus += 1

    def set_kierros_jarjestus(self, amount):
        self.kierros_jarjestus = amount
