import sys
from PyQt5.QtWidgets import QApplication

from gui import GUI
from game import Game

def main():

    global app
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())

main()
