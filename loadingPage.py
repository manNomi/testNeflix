import sys

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Loading:
    def __init__(self,ui):
        self.ui=ui
        self.indexNum=0
    def setMovie(self,num):
        self.timer =Loadingtime()
        self.ui.stackedWidget.setCurrentIndex(5)
        self.indexNum=num
        self.movie = QMovie("image/넷플릭스.gif", QByteArray())
        self.movie.setCacheMode(QMovie.CacheAll)
        self.ui.loginLogo.setMovie(self.movie)
        self.movie.start()
        self.timer.start()
        self.timer.time.connect(self.setTime)

    def setTime(self,time):
        if time==3:
            self.ui.stackedWidget.setCurrentIndex(self.indexNum)

class Loadingtime(QThread):
    time = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.num = 0           # 초깃값 설정
        self.num2=0
    def run(self):
        while True:
            self.time.emit(self.num)     # 방출
            print(self.num)
            self.num += 1
            time.sleep(1)
            if self.num>4:
                break
    

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Loading()
    Main.MainWindow.show()
    Main.movie.start()
    sys.exit(app.exec_())