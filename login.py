import mainUi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import find
import join
import playList

class Login:
    def __init__(self):
        self.ui=mainUi.Ui()
        self.loginClick()

    def loginClick(self):
        for index in range(0,len(self.ui.loginBtnList)):
            self.ui.loginBtnList[index].clicked.connect(lambda event,value=index : self.loginEvent(value))

    def loginEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.playList=playList.PlayList(self.ui)
            
        elif number==1:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.find=find.Find(self.ui)
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.join=join.Join(self.ui)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    start=Login()
    sys.exit(app.exec_())


# if __name__=="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     ui=mainUi.Ui()
#     ui.MainWindow.show()
#     sys.exit(app.exec_())