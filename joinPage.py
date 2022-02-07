import data
from PyQt5 import QtWidgets
class Join:
    def __init__(self,Ui,con):
        self.db=data.Database()
        self.ui=Ui
        self.con=con
        self.joinClick()
        self.changeTextEvent()
        self.dialog=QtWidgets.QDialog()
        self.id=self.ui.joinTextList[0].text()
        self.pw=self.ui.joinTextList[1].text()
        self.pwCheck=self.ui.joinTextList[2].text()
        self.name=self.ui.joinTextList[3].text()
        self.phone=self.ui.joinTextList[4].text()
        self.count=0


    def changeTextEvent(self):
        for index in range(0,len(self.ui.joinTextList)):
            self.ui.joinTextList[index].textChanged.connect(self.joinCheck)

    def joinClick(self):
        for index in range(0,len(self.ui.joinBtnList)):
            self.ui.joinBtnList[index].clicked.connect(lambda event,value=index : self.joinEvent(value))

    def joinEvent(self,number):
        if number==0:
            self.con.setTextClear()
            self.ui.stackedWidget.setCurrentIndex(0)
            #Back
        else:
            if self.count==5:
                memberData=[self.id,self.pw,self.name,self.phone]
                self.db.insertData("user",self.db.column1Value,memberData,self.db.cursor1,self.db.connect1)
                self.ui.stackedWidget.setCurrentIndex(0)
                self.con.setTextClear()
                self.ui.dialogCheck(self.dialog,"Congratulations.\nYou succeeded in signing up")
                self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
                self.dialog.exec()
            else:
                self.ui.dialogCheck(self.dialog,"Check error Input")
                self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
                self.dialog.exec()
            #Join
        

    def joinCheck(self,num):
        self.id=self.ui.joinTextList[0].text()
        self.pw=self.ui.joinTextList[1].text()
        self.pwCheck=self.ui.joinTextList[2].text()
        self.name=self.ui.joinTextList[3].text()
        self.phone=self.ui.joinTextList[4].text()

        IdRepeat=self.db.readData("user",["id"],[self.id],self.db.cursor1)
        PhoneRepeat=self.db.readData("user",["phone"],[self.phone],self.db.cursor1)
        count=0
        if len(IdRepeat)==0:
            self.ui.joinCheckText[0].setText("")
        else:
            self.ui.joinCheckText[0].setText("The same Id.")
            
        if len(PhoneRepeat)==0:
            self.ui.joinCheckText[4].setText("")
        else:
            self.ui.joinCheckText[4].setText("The same Phone Numbers.")


        if self.pw.isnumeric()==True or self.pw.isalpha()==True:
            self.ui.joinCheckText[1].setText("Pw must contain both numbers and letters")
            
        else:
            self.ui.joinCheckText[1].setText("")

        if len(list(self.id))<5 or len(list(self.id))>10 :
            self.ui.joinCheckText[0].setText("Id length must >5 and <10")
        else:
            self.ui.joinCheckText[0].setText("")
            

        if len(list(self.name))<2 or len(list(self.name))>10 :
            self.ui.joinCheckText[3].setText("Nickname length must >2 and <10")
        else:
            self.ui.joinCheckText[3].setText("")
            

        if len(list(self.pw))<5 or len(list(self.pw))>10 :
            self.ui.joinCheckText[1].setText("Password length must >5 and <10")

        elif self.pw!= self.pwCheck:
            self.ui.joinCheckText[1].setText("The password doesn't match")
            self.ui.joinCheckText[2].setText("The password doesn't match")
        else:
            self.ui.joinCheckText[1].setText("")
            self.ui.joinCheckText[2].setText("")


        if len(list(self.phone))!=11 :
            self.ui.joinCheckText[4].setText("phoneNumber must =11 EX)01012345678")

        elif self.phone.isnumeric()==False:
            self.ui.joinCheckText[4].setText("phoneNumber only combination INT")
        else:
            self.ui.joinCheckText[4].setText("")
         
        self.count=0
        for index in range (0,len(self.ui.joinCheckText)):
            if self.ui.joinCheckText[index].text()=="":
                self.count+=1
            else:
                self.count=0




        