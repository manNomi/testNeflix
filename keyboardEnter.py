import mainUi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

class KeyEvent:
    def __init__(self):
        self.setWindowTitle=("Keyboard Event")
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.ui.joinCheckText.setText("dkd")
        elif e.key() == Qt.Key_F:
            print("all")
        elif e.key() == Qt.Key_N:
            self.showNormal()