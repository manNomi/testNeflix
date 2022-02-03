import data
from PyQt5 import QtWidgets
class Join:
    def __init__(self,Ui):
        self.db=data.Database()
        self.ui=Ui
        self.joinClick()
        self.dialog=QtWidgets.QDialog()


    def joinClick(self):
        for index in range(0,len(self.ui.joinBtnList)):
            self.ui.joinBtnList[index].clicked.connect(lambda event,value=index : self.joinEvent(value))

    def joinEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(0)
            #Back
        else:
            id=self.ui.joinTextList[0].text()
            pw=self.ui.joinTextList[1].text()
            pwCheck=self.ui.joinTextList[2].text()
            name=self.ui.joinTextList[3].text()
            phone=self.ui.joinTextList[4].text()
            memberData=[id,pw,name,phone]
            self.db.insertData("user",self.db.column1Value,memberData,self.db.cursor1,self.db.connect1)
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.dialogCheck(self.dialog,"Congratulations.\nYou succeeded in signing up")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()
            #Join
        
            

