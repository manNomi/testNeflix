import VideoPage
from PyQt5 import QtWidgets
import data

class PlayList:
    def __init__(self,Ui,id):
        self.ui=Ui
        self.db=data.Database()
        self.id=id
        self.playListClick()
        self.dialog=QtWidgets.QDialog()
        self.dialog2=QtWidgets.QDialog()
        self.dialog3=QtWidgets.QDialog()


        


    def playListClick(self):
        # search update insert delete
        for index in range(0,len(self.ui.playListBtnList)):
            self.ui.playListBtnList[index].clicked.connect(lambda event,value=index : self.playListEvent(value))

        for index in range(0,len(self.ui.mainLogoListBtn)):
           self.ui.mainLogoListBtn[index].clicked.connect(lambda event,value=index : self.moveEvent(value))

        self.ui.playListBack.clicked.connect(self.backEvent)

    def playListEvent(self,number):
        if number==0:#search
            self.searchList()
        elif number==1:
            self.updateList()
        elif number==2:
            self.ui.dialogCheckEdit(self.dialog2,"insert")
            self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.insertPlayList())
            self.dialog2.exec()
        else:
            self.deleteList()

    def insertPlayList(self):
        listData=[self.id,self.ui.dialogText.text()]
        checkPlayListRepeat=self.db.readData("playList",["id","playList"],listData,self.db.cursor2)
        print(len(checkPlayListRepeat))
        if len(checkPlayListRepeat)==0:
            self.db.insertData("playList",self.db.column2Value,listData,self.db.cursor2,self.db.connect2)
            self.dialog2.close()
            self.playListSet()
        else:
            self.ui.dialogCheck(self.dialog3,"repeat")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()

    def playListSet(self):
        listData=self.db.readData("playList",["id"],[self.id],self.db.cursor2)
        playListText=[]
        for index in range (0,len(listData)):
            playListText.append(listData[index][2])
        self.ui.playList(playListText)



    def moveEvent(self,number):
        self.ui.stackedWidget.setCurrentIndex(4)
        video=VideoPage.Video(self.ui)
        
    def backEvent(self):
        self.ui.stackedWidget.setCurrentIndex(0)



    def searchList(self):
        self.ui.dialogPlayList(self.dialog,"search")
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.updateName())
        self.dialog.exec()

    def searchName(self):
        self.ui.dialogCheckEdit(self.dialog2,"search")
        self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.dialog2.close())
        self.dialog2.exec()
    



    def updateList(self):
        self.ui.dialogPlayList(self.dialog,"update")
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.updateName())
        self.dialog.exec()

    def updateName(self):
        self.ui.dialogCheckEdit(self.dialog2,"updateName")
        self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.dialog2.close())
        self.dialog2.exec()




    def deleteList(self):
        self.ui.dialogPlayList(self.dialog,"delete")
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.deleteName())
        self.dialog.exec()

    def deleteName(self):
        self.ui.dialogYesNo(self.dialog2,"delete?")
        self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.dialog2.close())
        self.dialog2.exec()
