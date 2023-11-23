import io
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.cu_dr)

    def paintEvent(self):
        pass

    def pesets(self):
        pass

