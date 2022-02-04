import mainUi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import findPage
import joinPage
import playListPage
import data

class Login:
    def __init__(self):
        self.db=data.Database()
        self.ui=mainUi.Ui()
        self.loginClick()
        self.dialog=QtWidgets.QDialog()
        self.join=joinPage.Join(self.ui)
        self.find=findPage.Find(self.ui)
        self.playList=playListPage.PlayList(self.ui)

    def loginClick(self):  # initEvent 
        for index in range(0,len(self.ui.loginBtnList)):
            self.ui.loginBtnList[index].clicked.connect(lambda event,value=index : self.loginEvent(value))

    def loginEvent(self,number):
        if number==0:
            self.loginCheckEvent()
        elif number==1:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)

    def loginCheckEvent(self):
        self.id,self.pw=self.ui.loginTextList[0].text(),self.ui.loginTextList[1].text()
        if  len(self.db.readData("user",["id","pw"],[self.id,self.pw],self.db.cursor1))!=0:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.playList.receiveId(self.id)
            self.playList.playListSet()
            self.playList.playListClick()

        else:
            self.ui.dialogCheck(self.dialog,"The ID and password are wrong")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    start=Login()
    sys.exit(app.exec_())

