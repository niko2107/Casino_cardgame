from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QLabel, QInputDialog
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from player import Player
from game import Game
from deck import Deck
from card import Card
from board import Board
from card_gui import Card_gui
from show_points import Show_points
from itertools import combinations

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(QWidget())
        self.init_window()
        self.init_buttons()
        self.show()

    def init_window(self):

        self.setGeometry(200, 100, 1000, 700)
        self.setWindowTitle('Kasino-peli')
        self.grid = QtWidgets.QGridLayout()
        self.setStyleSheet("background: url(Kuvat/card-4423492_1920.jpg)")
        self.centralWidget().setLayout(self.grid)

    def init_buttons(self):
        self.alkuteksti = QLabel()

        self.alkuteksti.setText("    Welcome!")
        self.grid.addWidget(self.alkuteksti, 1,0)
        self.alkuteksti.setStyleSheet("background: transparent")
        self.alkuteksti.setFont(QFont('Times',50))

        self.new_game_btn = QPushButton("New game")
        self.new_game_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.new_game_btn.setStyleSheet("border: 4px solid 'black';" +
        "border-radius: 15px; " +
        "font-size: 35px; color: 'white'")
        self.grid.addWidget(self.new_game_btn, 0, 0)
        self.new_game_btn.clicked.connect(lambda: self.start_new_game())

        self.load_game_btn = QPushButton("Load Game")
        self.grid.addWidget(self.load_game_btn, 0, 1)
        self.load_game_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.load_game_btn.setStyleSheet("border: 4px solid 'black';" +
        "border-radius: 15px; " +
        "font-size: 35px; color: 'white'")
        self.load_game_btn.clicked.connect(lambda: self.lataa_peli())

        self.exit_game_btn = QPushButton("Exit Game")
        self.exit_game_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_game_btn.setStyleSheet("border: 4px solid 'black';" +
        "border-radius: 15px; " +
        "font-size: 35px; color: 'white'")

        self.grid.addWidget(self.exit_game_btn, 0, 2)
        self.exit_game_btn.clicked.connect(QApplication.instance().quit)

    def start_new_game(self):
        self.peli = Game()

        player_amount, ok = QInputDialog.getInt(self, "New Game", "How many players? (2-8)")
        while True:
            if player_amount <= 8 and player_amount >= 2:
                break
            else:
                player_amount, ok = QInputDialog.getInt(self, "New Game", "Wrong amount of players! How many players? "
                                                                          "(2-8)")
        nimi_lista = []
        x=1
        while player_amount > 0:
            player_name, ok = QInputDialog.getText(self, "Player {}".format(x), "Enter name")
            while player_name in nimi_lista:
                player_name, ok = QInputDialog.getText(self, "Player {}".format(x), "Name already in use! Enter a new "
                                                                                    "name")
            nimi_lista.append(player_name)
            plr = Player(player_name)
            self.peli.add_player(plr)
            player_amount = player_amount - 1
            x+=1
        self.load_game_btn.hide()
        self.new_game_btn.hide()
        self.exit_game_btn.hide()

        self.pakka = Deck()
        self.pakka.create_deck()
        self.pakka.shuffle_deck()

        for pelaaja in self.peli.get_players():
            pelaaja.add_cards_to_hand(self.pakka.deal(4))

        self.lauta = Board()
        self.lauta.add_cards_to_board(self.pakka.deal(4))
        self.game_window()

    def game_window(self):
        self.alkuteksti.hide()
        self.window = QtWidgets.QGraphicsScene()
        self.window.setSceneRect(0,0,350,500)

        self.view = QtWidgets.QGraphicsView(self.window, self)
        self.view.adjustSize()
        self.view.setStyleSheet("background-image: url(Kuvat/Kasino_tausta.jpg)")
        self.setStyleSheet("background: darkred")
        self.view.show()
        self.grid.addWidget(self.view,0,0)

        self.play_card_btn = QPushButton("Play Card")
        self.play_card_btn.setStyleSheet("color : orange; background : black")
        self.play_card_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.play_card_btn, 1,0)
        self.play_card_btn.clicked.connect(lambda: self.press_play_card_btn())

        self.card_to_table_btn = QPushButton("Put The Card On The Table")
        self.card_to_table_btn.setStyleSheet("color : orange; background : black")
        self.card_to_table_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.card_to_table_btn, 2,0)
        self.card_to_table_btn.clicked.connect(lambda: self.press_card_to_table_btn())

        self.save_gm_btn = QPushButton("Save Game")
        self.save_gm_btn.setStyleSheet("color : orange; background : black")
        self.save_gm_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.save_gm_btn,1,1)
        self.save_gm_btn.clicked.connect(lambda: self.tallenna_peli())

        self.show_pnts_btn = QPushButton("Show Points")
        self.show_pnts_btn.setStyleSheet("color : orange; background : black")
        self.show_pnts_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.show_pnts_btn, 2, 1)
        self.show_pnts_btn.clicked.connect(lambda: self.show_points())

        self.next_turn_btn = QPushButton("Next Turn")
        self.next_turn_btn.setStyleSheet("color : orange; background : black")
        self.next_turn_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.next_turn_btn, 3, 0)
        self.next_turn_btn.clicked.connect(lambda: self.press_next_turn_btn())

        self.exit_game = QPushButton("Exit")
        self.exit_game.setStyleSheet("color : orange; background : black")
        self.exit_game.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid.addWidget(self.exit_game,3,1)
        self.exit_game.clicked.connect(QApplication.instance().quit)

        poyta_kortit = self.lauta.return_cards()
        x=0
        for kortti in poyta_kortit:
            card=Card_gui(kortti)
            self.lauta.add_gui_card(card)
            self.window.addWidget(card)
            card.move(-150 + 120*x,0)
            x+=1

        self.luo_alkukasi()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.uptate_all())
        self.timer.start(20)  # kutsutaan funktiota 10 ms välein

        a = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()
        self.pelaajan_nimi_qlabel = QLabel("Player turn: {}".format(pelaaja_lista[a].get_name()))
        self.window.addWidget(self.pelaajan_nimi_qlabel)
        self.pelaajan_nimi_qlabel.setFont(QFont('Times',20))
        self.pelaajan_nimi_qlabel.move(-200,400)

        self.pakan_tiedot_qlabel = QLabel("Cards left on the deck: {}".format(self.pakka.cards_left()))
        self.window.addWidget(self.pakan_tiedot_qlabel)
        self.pakan_tiedot_qlabel.setFont(QFont('Times',20))
        self.pakan_tiedot_qlabel.move(-200,500)

    def luo_alkukasi(self):
        pelaajien_lkm = self.peli.count_players()
        a = self.peli.get_player_turn()
        y = 0
        pelaaja_lista = self.peli.get_players()
        pelaaja_lista[a].muuta_alku_kasi()

        for kortti in pelaaja_lista[a].get_player_hand():
            card = Card_gui(kortti)
            pelaaja_lista[a].add_gui_card(card)
            self.window.addWidget(card)
            card.move(50 + 120 * y, 350)
            y += 1

    def piilota_kasi(self):
        a = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()

        for kortti in pelaaja_lista[a].get_player_gui_cards():
            kortti.hide()

    def nayta_kasi(self):
        a = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()

        for kortti in pelaaja_lista[a].get_player_gui_cards():
            kortti.show()

    def uptate_all(self):
        pelaajan_numero = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()
        pelaajan_kasi = pelaaja_lista[pelaajan_numero].get_player_gui_cards()

        y = 0
        true_kortti_lista = []
        for gui_kortti in pelaajan_kasi:
            if gui_kortti.onko_klikattu() == True:
                true_kortti = gui_kortti
                true_kortti_lista.append(true_kortti)
                if len(true_kortti_lista) > 1:
                    true_kortti_lista[0].click_card()
                    del true_kortti_lista[0] # muokataan vielä

                gui_kortti.move(50 + 120 * y, 320)
                y += 1

            elif gui_kortti.onko_klikattu() == False:
                gui_kortti.move(50 + 120 * y, 350)
                y += 1

        poyta_kortit = self.lauta.return_gui_cards()
        x=0
        for gui_kortti in poyta_kortit:

            if gui_kortti.onko_klikattu() == True:
                gui_kortti.move(-250 + 120 * x, -30)
                x += 1

            elif gui_kortti.onko_klikattu() == False:
                gui_kortti.move(-250 + 120 * x, 0)
                x += 1

    def press_play_card_btn(self):
        # Ruutu-10 kädessä = 16, Pata-2 kädessä = 15, Ässät kädessä = 14

        pelaajan_numero = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()

        if pelaaja_lista[pelaajan_numero].onko_vuoro_pelattu() == True:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Player has already played this turn!')
            self.window.addWidget(error_dialog)
            error_dialog.move(100, 100)

        elif pelaaja_lista[pelaajan_numero].onko_vuoro_pelattu() == False:

            pelaajan_kasi = pelaaja_lista[pelaajan_numero].get_player_gui_cards()

            testaus_lista = []
            for gui_kortti in pelaajan_kasi: # etsitään pelaajan klikattu kortti
                if gui_kortti.onko_klikattu() == True:
                    testaus_lista.append(gui_kortti)
                    gui_kortti.click_card()
                    card = gui_kortti.get_card()
                    gui_card = gui_kortti

            if len(testaus_lista) == 0:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Player must pick a card!')
                self.window.addWidget(error_dialog)
                error_dialog.move(100, 100)

            else:
                card = self.check_special_card(card)

                true_gui_kortit = []
                true_kortit = []
                poyta_kortit = self.lauta.return_gui_cards()
                for gui_tablecard in poyta_kortit: # etsitään pöydältä klikatut kortit
                    if gui_tablecard.onko_klikattu() == True:
                        gui_tablecard.click_card()

                        true_gui_kortit.append(gui_tablecard) # kerätään listään klikatut kortit
                        true_card = gui_tablecard.get_card()
                        if true_card.get_card_value() == 16: # ruutu_10
                            true_card.change_card_value(10)
                        if true_card.get_card_value() == 15:
                            true_card.change_card_value(2)
                        true_kortit.append(true_card)

                summa = 0
                for testi_kortti in true_kortit:
                    summa = summa + testi_kortti.get_card_value()
                if summa == 0:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Player must pick cards from board!')
                    self.window.addWidget(error_dialog)
                    error_dialog.move(100, 100)
                else:
                    if self.check_combination(card.get_card_value(), true_kortit) == True:

                        pelaaja_lista[pelaajan_numero].muuta_vuoro_pelattu()
                        pelaaja_lista[pelaajan_numero].remove_card_from_hand(card)
                        gui_card.hide()
                        pelaaja_lista[pelaajan_numero].remove_gui_card(gui_card)

                        for plr in pelaaja_lista:
                            plr.nollaa_nostanut_poydasta()
                        pelaaja_lista[pelaajan_numero].nostaa_poydasta()


                        for x in true_kortit:
                            pelaaja_lista[pelaajan_numero].collect_card()
                            self.lauta.remove_card_from_table(x)
                            if self.lauta.return_len_table_cards() == 0:
                                pelaaja_lista[pelaajan_numero].add_cottage()
                            if x.get_card_value() == 1:
                                pelaaja_lista[pelaajan_numero].lisaa_assa()
                            if x.get_card_suit() == 'S':
                                pelaaja_lista[pelaajan_numero].lisaa_pata() # lisätään padat ja ässät pöydästä
                            if x.get_card_suit() == 'S' and x.get_card_value() == 2:
                                pelaaja_lista[pelaajan_numero].lisaa_pata_2()
                            if x.get_card_suit() == 'D' and x.get_card_value() == 10:
                                pelaaja_lista[pelaajan_numero].lisaa_ruutu_10()
                        pelaaja_lista[pelaajan_numero].collect_card()

                        if card.get_card_value() == 14:  # lisätään ässä kädestä
                            pelaaja_lista[pelaajan_numero].lisaa_assa()
                        if card.get_card_suit() == 'S':
                            pelaaja_lista[pelaajan_numero].lisaa_pata()  # lisätään pata kädestä
                        if card.get_card_value() == 16:
                            pelaaja_lista[pelaajan_numero].lisaa_ruutu_10()
                        if card.get_card_value() == 15:
                            pelaaja_lista[pelaajan_numero].lisaa_pata_2()

                        for y in true_gui_kortit:
                            y.hide()
                            self.lauta.remove_gui_card(y)

                        if self.pakka.cards_left() != 0:
                            jaettava_kortti = self.pakka.deal(1)
                            jaettava_gui_kortti = Card_gui(jaettava_kortti[0])
                            pelaaja_lista[pelaajan_numero].add_one_card_to_hand(jaettava_kortti[0])
                            pelaaja_lista[pelaajan_numero].add_gui_card(jaettava_gui_kortti)
                            self.window.addWidget(jaettava_gui_kortti)

                            self.pakan_tiedot_qlabel.setText(
                                "Cards left on the deck: {}".format(self.pakka.cards_left()))
                            self.pakan_tiedot_qlabel.adjustSize()

    def check_combination(self, value, cards):

        onnistuneet_kombot = []
        for a in range(1, len(cards)+1):
            kombot = combinations(cards, a) # etsitään kaikki mahdolliset yhdistelmät joita valituista korteista saa
            for pikku_lista in kombot: # tarkistetaan yhtä yhdistelmää kerrallaan
                summa = 0
                for yksittainen_kortti in pikku_lista: # summataan yhdistelmän korttien arvot yhteen
                    summa += yksittainen_kortti.get_card_value()
                if summa == value: # jos korttien summa on sama kuin pelaajan kortin arvo lisätään listaan
                    onnistuneet_kombot.append(pikku_lista)

        pituus = len(cards) # valittujen korttien määrä
        lista_2 = []
        for b in range(1, len(onnistuneet_kombot)+1):
            kombo = combinations(onnistuneet_kombot, b) # tehdään yhdistelmiä onnistuneista yhdistelmistä
            for iso_alkio in kombo: # otetaan yksi yhdistelmä
                summa = 0
                for alkio in iso_alkio: # alkio on yksi mahdollinen yhdistelmä kokonaisuus
                    summa += len(alkio) # summataan alkioden määrä
                if summa == pituus: # tarkistetaan milloin alkioiden määrä on sama kuin valittujen korttien määrä
                    lista_2.append(iso_alkio)

        true_lista = []
        for joukko in lista_2: # käydään läpi listaa, jossa alkioiden määrä on sama kuin valittujen korttien määrä
            loyto = [False]*pituus # alustetaan löydetyt kortit Falseksi
            for kortti in cards: # käydään läpi jokainen kortti jonka pelaaja on valinnut
                for part in joukko:
                    if kortti in part: # jos kortti löytyy listasta, asetetaan se löydetyksi eli Trueksi
                        loyto[cards.index(kortti)] = True
            if not False in loyto: # lisätään löydetyt (True) kortit listaan
                true_lista.append(joukko)

        return len(true_lista) != 0 # jos oikeita yhdistelmiä löytynyt palauttaa True, jos ei palauttaa False

    def check_special_card(self, kortti):
        # Ruutu-10 kädessä = 16, Pata-2 kädessä = 15, Ässät kädessä = 14
        if kortti.get_card_value() == 1:
            kortti.change_card_value(14) # kortti on ässä
        elif kortti.get_card_value() == 10:
            if kortti.get_card_suit() == 'D': # ruutu-10
                kortti.change_card_value(16)
        elif kortti.get_card_value() == 2:
            if kortti.get_card_suit() == 'S':
                kortti.change_card_value(15)
        return kortti

    def press_card_to_table_btn(self):
        pelaajan_numero = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()

        if pelaaja_lista[pelaajan_numero].onko_vuoro_pelattu() == True:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Player has already played this turn!')
            self.window.addWidget(error_dialog)
            error_dialog.move(100, 100)

        elif pelaaja_lista[pelaajan_numero].onko_vuoro_pelattu() == False:

            pelaajan_kasi = pelaaja_lista[pelaajan_numero].get_player_gui_cards()

            testaus_lista = []
            for gui_kortti in pelaajan_kasi:
                if gui_kortti.onko_klikattu() == True:
                    testaus_lista.append(gui_kortti)
                    gui_kortti.click_card()
                    card = gui_kortti.get_card()
                    self.lauta.add_one_card_to_board(card)
                    self.lauta.add_gui_card(gui_kortti)

                    if self.pakka.cards_left() != 0:
                        jaettava_kortti = self.pakka.deal(1)
                        jaettava_gui_kortti = Card_gui(jaettava_kortti[0])
                        pelaaja_lista[pelaajan_numero].add_one_card_to_hand(jaettava_kortti[0])
                        pelaaja_lista[pelaajan_numero].add_gui_card(jaettava_gui_kortti)
                        self.window.addWidget(jaettava_gui_kortti)

                        self.pakan_tiedot_qlabel.setText("Cards left on the deck: {}".format(self.pakka.cards_left()))
                        #self.pakan_tiedot_qlabel.adjustSize()

                    pelaaja_lista[pelaajan_numero].remove_gui_card(gui_kortti)
                    pelaaja_lista[pelaajan_numero].remove_card_from_hand(card)

            if len(testaus_lista) == 0:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Player must pick a card!')
                self.window.addWidget(error_dialog)
                error_dialog.move(100, 100)
            else:
                pelaaja_lista[pelaajan_numero].muuta_vuoro_pelattu()

    def press_next_turn_btn(self):
        pelaaja_lista = self.peli.get_players()
        nykyinen_pelaaja = self.peli.get_player_turn()
        if pelaaja_lista[nykyinen_pelaaja].onko_vuoro_pelattu() == False:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Player must play first!')
            self.window.addWidget(error_dialog)
            error_dialog.move(100,100)

        elif pelaaja_lista[nykyinen_pelaaja].onko_vuoro_pelattu() == True:
            pelaaja_lista[nykyinen_pelaaja].muuta_vuoro_pelattu()
            self.piilota_kasi()
            self.peli.next_player_turn()
            pelaajan_numero = self.peli.get_player_turn()
            if len(pelaaja_lista[pelaajan_numero].get_player_hand()) == 0: # katsotaan onko kierros loppunut
                self.kierros_loppu()
            elif len(pelaaja_lista[pelaajan_numero].get_player_hand()) != 0:
                self.pelaajan_nimi_qlabel.setText("Player turn: {}".format(pelaaja_lista[pelaajan_numero].get_name()))
                self.pelaajan_nimi_qlabel.adjustSize()

                if pelaaja_lista[pelaajan_numero].onko_alku_kasi_luotu() == False:
                    self.luo_alkukasi()
                elif pelaaja_lista[pelaajan_numero].onko_alku_kasi_luotu() == True:
                    self.nayta_kasi()

    def tallenna_peli(self):
        teksti, ok = QInputDialog.getText(self, "Save Game", "Give game a name")
        if ok:
            teksti = teksti.strip()
            if len(teksti) != 0:
                teksti = teksti+".txt"
                tiedosto = open(teksti,"w") # luodaaan tiedosto johon kirjoitetaan

                pelaajan_vuoro = self.peli.get_player_turn()
                tiedosto.write(str(pelaajan_vuoro))
                tiedosto.write("\n")
                tiedosto.write("#")
                tiedosto.write("\n")

                pelaaja_lista = self.peli.get_players()
                for pelaaja in pelaaja_lista:
                    tiedosto.write(pelaaja.get_name())
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.get_player_collected_cards()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.get_player_score()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_cottages()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_padat()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_assat()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_ruutu_10()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_pata_2()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.return_nostaa_poydasta()))
                    tiedosto.write(" ")
                    tiedosto.write(str(pelaaja.onko_vuoro_pelattu()))
                    tiedosto.write(" # ")
                    for kortti in pelaaja.get_player_hand():
                        tiedosto.write(kortti.get_card_suit())
                        tiedosto.write(" ")
                        tiedosto.write(str(kortti.get_card_value()))
                        tiedosto.write(" ")
                    tiedosto.write("\n")

                tiedosto.write("#")
                tiedosto.write("\n")

                poyta_kortit = self.lauta.return_cards()
                for kortti in poyta_kortit:
                    tiedosto.write(kortti.get_card_suit())
                    tiedosto.write(" ")
                    tiedosto.write(str(kortti.get_card_value()))
                    tiedosto.write(" ")
                    tiedosto.write("\n")

                tiedosto.write("#")
                tiedosto.write("\n")

                pakka_kortit = self.pakka.return_deck()
                for kortti in pakka_kortit:
                    tiedosto.write(kortti.get_card_suit())
                    tiedosto.write(" ")
                    tiedosto.write(str(kortti.get_card_value()))
                    tiedosto.write(" ")
                    tiedosto.write("\n")
                tiedosto.write("#") # päätösmerkki
                tiedosto.close()

    def lataa_peli(self):
        teksti, ok = QInputDialog.getText(self, "Load Game", "Give game a name")
        if ok:
            teksti=teksti.strip()
            teksti += '.txt'
            try:
                with open(teksti) as tiedosto:
                    self.peli = Game()
                    self.load_game_btn.hide()
                    self.new_game_btn.hide()
                    self.exit_game_btn.hide()
                    self.pakka = Deck()
                    self.lauta = Board()
                     # alustetaan pelitilanne

                    rivi = tiedosto.readline()
                    rivi = rivi.strip()
                    pelaajan_vuoro = int(rivi)
                    self.peli.set_player_turn(pelaajan_vuoro)

                    rivi = tiedosto.readline() # ensimmäinen #-merkki
                    rivi = tiedosto.readline()
                    rivi = rivi.split(" ")
                    while len(rivi) != 1:
                        pelaajan_nimi = rivi[0]
                        pelaaja = Player(pelaajan_nimi)
                        self.peli.add_player(pelaaja)
                        pelaajan_keratut_kortit = int(rivi[1])
                        pelaaja.set_keratut_kortit(pelaajan_keratut_kortit)
                        pelaajan_pisteet = int(rivi[2])
                        pelaaja.set_score(pelaajan_pisteet)
                        pelaajan_mokit = int(rivi[3])
                        pelaaja.set_cottages(pelaajan_mokit)
                        pelaajan_padat = int(rivi[4])
                        pelaaja.set_padat(pelaajan_padat)
                        pelaajan_assat = int(rivi[5])
                        pelaaja.set_assat(pelaajan_assat)

                        ruutu_10 = int(rivi[6])
                        pelaaja.set_ruutu_10(ruutu_10)
                        pata_2 = int(rivi[7])
                        pelaaja.set_pata_2(pata_2)
                        nostanut = int(rivi[8])
                        pelaaja.set_nostaa_poydasta(nostanut)

                        pelaajan_onko_vuoro_pelattu = str(rivi[9])
                        pelaaja.set_onko_vuoro_pelattu(pelaajan_onko_vuoro_pelattu)

                        x = 11
                        while rivi[x] != '\n':
                            kortti_maa = rivi[x]
                            kortti_arvo = int(rivi[x+1])
                            kortti = Card(kortti_maa,kortti_arvo)
                            pelaaja.add_one_card_to_hand(kortti)
                            x += 2

                        rivi = tiedosto.readline()
                        rivi = rivi.split(" ") # luettu viimeinen pelaaja ja viimeinen kortti

                    rivi = tiedosto.readline()
                    rivi = rivi.split(" ")

                    if len(rivi[0]) == 1: # tarkistetaan että pöydässä on kortteja, nyt on

                        while len(rivi[0]) == 1: # luetaan #-merkkiin asti
                            poyta_kortti_maa = rivi[0]
                            poyta_kortti_arvo = int(rivi[1])
                            kortti = Card(poyta_kortti_maa, poyta_kortti_arvo)
                            self.lauta.add_one_card_to_board(kortti)
                            rivi = tiedosto.readline()
                            rivi = rivi.split(" ")

                    rivi = tiedosto.readline() # alkaa pakan luku
                    rivi = rivi.split(" ")

                    if len(rivi[0]) == 1: # pakassa kortteja

                        while rivi[0] != '#':

                            pakka_kortti_maa = rivi[0]
                            pakka_kortti_arvo = int(rivi[1])
                            kortti = Card(pakka_kortti_maa, pakka_kortti_arvo)
                            self.pakka.add_card_to_deck(kortti)
                            rivi = tiedosto.readline()
                            rivi = rivi.split(" ")

                    self.game_window() # luodaan uusi pelinäkymä

            except OSError:
                teksti = "The file does not exist!"
                ilmoitus = QtWidgets.QMessageBox()
                ilmoitus.setWindowTitle("Error!")
                ilmoitus.setIcon(QtWidgets.QMessageBox.Warning)
                ilmoitus.setText(teksti)
                ilmoitus.setGeometry(800, 400, 400, 300)
                ilmoitus.exec()

    def kierros_loppu(self):
        self.timer.stop()
        self.lauta.nollaa_table_cards()
        gui_poyta_kortit = self.lauta.return_gui_cards()
        kortteja_jaljella = len(gui_poyta_kortit)
        pelaajat = self.peli.get_players()
        for pelaaja in pelaajat:
            if pelaaja.return_nostaa_poydasta() == 1:
                for card in gui_poyta_kortit:
                    card = card.get_card()
                    if card.get_card_value() == 16 and card.get_card_suit() == 'D':
                        pelaaja.lisaa_ruutu_10()
                    if card.get_card_suit() == 'S':
                        pelaaja.lisaa_pata()
                    if card.get_card_suit() == 'S' and card.get_card_value() == 15:
                        pelaaja.lisaa_pata_2()
                    if card.get_card_value() == 1:
                        pelaaja.lisaa_assa()
                pelaaja.collect_multiple_cards(kortteja_jaljella)

        for gui_kortti in gui_poyta_kortit:
            gui_kortti.hide()

        self.lauta.nollaa_table_cards_gui()
        self.pelaajan_nimi_qlabel.hide()
        self.pakan_tiedot_qlabel.hide()
        self.laske_pisteet()

        peli_loppu = 0
        for plr in pelaajat:
            if plr.get_player_score() > 15:
                peli_loppu += 1
                self.peli_loppu()

        self.show_points()
        self.nollaa_tiedot()
        if peli_loppu == 0:
            self.aloita_uusi_peli()

    def laske_pisteet(self):
        pelaaja_lista = self.peli.get_players()
        keratut_kortit = 0
        keratut_padat = 0
        pelaaja_eniten_kortteja = None
        pelaaja_eniten_patoja = None
        for pelaaja in pelaaja_lista:
            mokit = pelaaja.return_cottages()
            pelaaja.uptate_score(mokit)
            assat = pelaaja.return_assat()
            pelaaja.uptate_score(assat)
            if pelaaja.get_player_collected_cards() > keratut_kortit:
                keratut_kortit = pelaaja.get_player_collected_cards()
                pelaaja_eniten_kortteja = pelaaja
            if pelaaja.return_padat() > keratut_padat:
                keratut_padat = pelaaja.return_padat()
                pelaaja_eniten_patoja = pelaaja
            ruutu_10 = pelaaja.return_ruutu_10()
            if ruutu_10 == 1:
                pelaaja.uptate_score(2)
            pata_2 = pelaaja.return_pata_2()
            if pata_2 == 1:
                pelaaja.uptate_score(1)

        pelaaja_eniten_kortteja.uptate_score(1)
        pelaaja_eniten_patoja.uptate_score(2)

    def nollaa_tiedot(self):
        pelaaja_lista = self.peli.get_players()
        for pelaaja in pelaaja_lista:
            pelaaja.set_cottages(0)
            pelaaja.set_assat(0)
            pelaaja.set_keratut_kortit(0)
            pelaaja.set_padat(0)
            pelaaja.set_ruutu_10(0)
            pelaaja.set_pata_2(0)
            pelaaja.alku_kasi_ei_luotu()

    def aloita_uusi_peli(self):
        self.timer.start()

        teksti = "This round is over!\nStart new round"
        ilmoitus = QtWidgets.QMessageBox()
        ilmoitus.setWindowTitle("Round over")
        ilmoitus.setIcon(QtWidgets.QMessageBox.Information)
        ilmoitus.setText(teksti)
        ilmoitus.setGeometry(800, 400, 500, 400)
        ilmoitus.exec()

        pelaajien_lkm = self.peli.count_players()
        kierros_jarjestus = self.peli.get_kierros_jarjestus()
        if kierros_jarjestus > pelaajien_lkm:
            self.peli.set_kierros_jarjestus(0)
        self.peli.set_player_turn(kierros_jarjestus)
        self.peli.add_kierros_jarjestus()

        self.pakka.create_deck()
        self.pakka.shuffle_deck()

        for pelaaja in self.peli.get_players():
            jaettavat_kortit = self.pakka.deal(4)
            pelaaja.add_cards_to_hand(jaettavat_kortit)

        self.luo_alkukasi()
        self.lauta.add_cards_to_board(self.pakka.deal(4))

        poyta_kortit = self.lauta.return_cards()
        x = 0
        for kortti in poyta_kortit:
            card = Card_gui(kortti)
            self.lauta.add_gui_card(card)
            self.window.addWidget(card)
            card.move(-150 + 120 * x, 0)
            x += 1

        a = self.peli.get_player_turn()
        pelaaja_lista = self.peli.get_players()
        self.pelaajan_nimi_qlabel = QLabel("Player turn: {}".format(pelaaja_lista[a].get_name()))
        self.window.addWidget(self.pelaajan_nimi_qlabel)
        self.pelaajan_nimi_qlabel.setFont(QFont('Times', 20))
        self.pelaajan_nimi_qlabel.move(-200, 400)

        self.pakan_tiedot_qlabel = QLabel("Cards left on the deck: {}".format(self.pakka.cards_left()))
        self.window.addWidget(self.pakan_tiedot_qlabel)
        self.pakan_tiedot_qlabel.setFont(QFont('Times', 20))
        self.pakan_tiedot_qlabel.move(-200, 500)

    def peli_loppu(self):
        voittaja = None
        pisteet = 0
        pelaaja_lista = self.peli.get_players()
        for pelaaja in pelaaja_lista:
            if pelaaja.get_player_score() > pisteet:
                pisteet = pelaaja.get_player_score()
                voittaja = pelaaja

        self.nollaa_tiedot()
        teksti = "Winner is {} with {} points.\nWell played!".format(voittaja.get_name(),voittaja.get_player_score())
        ilmoitus = QtWidgets.QMessageBox()
        ilmoitus.setWindowTitle("Winner")
        ilmoitus.setIcon(QtWidgets.QMessageBox.Information)
        ilmoitus.setText(teksti)
        ilmoitus.setGeometry(800, 400, 500, 400)
        ilmoitus.exec()

        self.play_card_btn.hide()
        self.card_to_table_btn.hide()
        self.save_gm_btn.hide()
        self.next_turn_btn.hide()

    def show_points(self):
        pelaajat = self.peli.get_players()
        self.pinnat = Show_points(pelaajat)



























