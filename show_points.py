import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.Qt import QLabel
from player import Player

class Show_points(QWidget):

    def __init__(self, pelaaja_lista):
        super().__init__()

        self.pelaaja_lista = pelaaja_lista
        self.print()
        self.show()

    def print(self):

        self.vertical = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.vertical)

        self.setWindowTitle("Points in this game")

        assat = QLabel()
        assat.setText('Aces')
        mokit = QLabel()
        mokit.setText('Cottages')
        padat = QLabel()
        padat.setText('Spades')
        points = QLabel()
        points.setText('Points')
        ruutu_10 = QLabel()
        ruutu_10.setText("10 of Diamonds")
        pata_2 = QLabel()
        pata_2.setText("2 of Spades")
        kortit = QLabel()
        kortit.setText('Collected cards')

        self.grid.addWidget(assat, 1, 0)
        self.grid.addWidget(padat, 2, 0)
        self.grid.addWidget(mokit, 3, 0)
        self.grid.addWidget(kortit, 4, 0)
        self.grid.addWidget(ruutu_10, 5, 0)
        self.grid.addWidget(pata_2, 6, 0)
        self.grid.addWidget(points, 7, 0)

        x = 1
        for pelaaja in self.pelaaja_lista:
            nimi = QLabel()
            nimi.setText("{:s}".format(pelaaja.get_name()))

            pelaajan_assat = QLabel()
            pelaajan_assat.setText("{:d}".format(pelaaja.return_assat()))

            pelaajan_padat = QLabel()
            pelaajan_padat.setText("{:d}".format(pelaaja.return_padat()))

            pelaajan_mokit = QLabel()
            pelaajan_mokit.setText("{:d}".format(pelaaja.return_cottages()))

            pelaajan_keratut_kortit = QLabel()
            pelaajan_keratut_kortit.setText("{:d}".format(pelaaja.get_player_collected_cards()))

            pelaajan_ruutu_10 = QLabel()
            pelaajan_ruutu_10.setText("{:d}".format(pelaaja.return_ruutu_10()))

            pelaajan_pata_2 = QLabel()
            pelaajan_pata_2.setText("{:d}".format(pelaaja.return_pata_2()))

            pisteet = QLabel()
            pisteet.setText("{:d}".format(pelaaja.get_player_score()))

            self.grid.addWidget(nimi, 0, x)
            self.grid.addWidget(pelaajan_assat, 1, x)
            self.grid.addWidget(pelaajan_padat, 2, x)
            self.grid.addWidget(pelaajan_mokit, 3, x)
            self.grid.addWidget(pelaajan_keratut_kortit, 4, x)
            self.grid.addWidget(pelaajan_ruutu_10, 5, x)
            self.grid.addWidget(pelaajan_pata_2, 6, x)
            self.grid.addWidget(pisteet, 7, x)

            x += 1

        self.vertical.addLayout(self.grid)


