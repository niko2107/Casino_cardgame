from PyQt5.Qt import QLabel, QPixmap
from card import Card

class Card_gui(QLabel):

    def __init__(self, kortti):
        super(Card_gui,self).__init__()
        self.kortti = kortti
        self.maa = self.kortti.get_card_suit()
        self.arvo = self.kortti.get_card_value()
        self.create_card_gui(self.maa, self.arvo)
        self.klikattu = False

    def create_card_gui(self, maa, arvo):
        teksti ="Kuvat/PNG/"
        erikoiskortit = [1,11,12,13]
        if arvo not in erikoiskortit:
            teksti += str(arvo)
            teksti += maa
            teksti += ".png"
        elif arvo == 1:
            teksti += "A"
            teksti += maa
            teksti += ".png"
        elif arvo == 11:
            teksti += "J"
            teksti += maa
            teksti += ".png"
        elif arvo == 12:
            teksti += "Q"
            teksti += maa
            teksti += ".png"
        elif arvo == 13:
            teksti += "K"
            teksti += maa
            teksti += ".png"

        kuva = QPixmap(teksti)
        self.setPixmap(kuva.scaled(100,150))

    def mousePressEvent(self, *args,**kwargs):
        self.click_card()

    def click_card(self):
        if self.klikattu == False:
            self.klikattu = True
        else:
            self.klikattu = False

    def onko_klikattu(self):
        return self.klikattu

    def get_card(self):
        return self.kortti






