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
            
            memberData=[id,pw,name,phone]
            self.db.insertData("user",self.db.column1Value,memberData,self.db.cursor1,self.db.connect1)
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.dialogCheck(self.dialog,"Congratulations.\nYou succeeded in signing up")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.dialog.exec()
            #Join
        
            

    def joinCheck(self):
        id=self.ui.joinTextList[0].text()
        pw=self.ui.joinTextList[1].text()
        pwCheck=self.ui.joinTextList[2].text()
        name=self.ui.joinTextList[3].text()
        phone=self.ui.joinTextList[4].text()

        IdRepeat=self.db.readData("user",["id"],[id],self.db.cursor1)
        PhoneRepeat=self.db.readData("user",["phone"],[phone],self.db.cursor1)
        count=0
        if len(IdRepeat)==0:
            count+=1
        else:
            text="The same Id."
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        if len(PhoneRepeat)==0:
            count+=1
        else:
            text="The same Phone Numbers."
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()

        if pw.isnumeric()==True or pw.isalpha()==True:
            text="Pw must contain both numbers and letters"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        else:count+=1


        if len(list(id))<5 or len(list(id))>10 :
            text="Id length must >5 and <10"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        else:
            count+=1

        if len(list(name))<2 or len(list(name))>10 :
            text="Nickname length must >2 and <10"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        else:
            count+=1

        if len(list(pw))<5 or len(list(pw))>10 :
            text="Password length must >5 and <10"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()

        elif pw!= pwCheck:
            text="The password doesn't match"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        else:
            count+=1

        if len(list(phone))!=11 :
            text="phoneNumber must =11 EX)01012345678"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        elif self.myPhone.isnumeric()==False:
            text="phoneNumber only combination INT"
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog.close())
            self.ui.dialogCheck(self.dialog,text)
            self.dialog.exec()
        else:
            count+=1

        