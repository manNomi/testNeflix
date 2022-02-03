import data
from PyQt5 import QtWidgets
class Find:
    def __init__(self,Ui):
        self.ui=Ui
        self.findClick()
        self.db=data.Database()
        self.dialog=QtWidgets.QDialog()

    def findClick(self): ## initEvent 로 통일 
        for index in range(0,len(self.ui.findBtnList)):
            self.ui.findBtnList[index].clicked.connect(lambda event,value=index : self.findEvent(value))

    def findEvent(self,number):
        if number==0:
            self.findPwEvent()
            #find PW
        elif number==1:
            self.findIdEvent()
            #find ID
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def findIdEvent(self):
        phone=self.ui.findTextID[0].text()
        name=self.ui.findTextID[1].text()
        id=self.db.readData("user",["phone","name"],[phone,name],self.db.cursor1)
        if len(id)==0:
            self.ui.dialogCheck(self.dialog,"Incorrect input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()
        else:
            text="ID="+str(id[0][1])
            self.ui.dialogCheck(self.dialog,text)
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()

    def findPwEvent(self):
        phone=self.ui.findTextPW[0].text()
        name=self.ui.findTextPW[1].text()
        id=self.ui.findTextPW[2].text()
        pw=self.db.readData("user",["id","phone","name"],[id,phone,name],self.db.cursor1)
        if len(pw)==0:
            self.ui.dialogCheck(self.dialog,"Incorrect input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()
        else:
            text="Pw="+str(pw[0][2])
            self.ui.dialogCheck(self.dialog,text)
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()