import VideoPage
from PyQt5 import QtWidgets
import data

class PlayList:
    def __init__(self,Ui):
        self.ui=Ui
        self.db=data.Database()
        self.ui.playListBack.clicked.connect(self.backEvent)
        for index in range(0,len(self.ui.playListBtnList)):
            self.ui.playListBtnList[index].clicked.connect(lambda event,value=index : self.playListEvent(value))
        self.dialog=QtWidgets.QDialog()
        self.dialog2=QtWidgets.QDialog()
        self.dialog3=QtWidgets.QDialog()
        self.id=None
        self.playListText=[]

    def receiveId(self,id):
        self.id=id        
        self.playListClick()

    def playListClick(self):
        # search update insert delete
        for index in range(0,len(self.ui.mainLogoListBtn)):
           self.ui.mainLogoListBtn[index].clicked.connect(lambda event,value=index : self.moveEvent(value))

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
        self.playListText=[]
        for index in range (0,len(listData)):
            self.playListText.append(listData[index][2])
        self.ui.playList(self.playListText)

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
        self.ui.dialogPlayList(self.dialog,"update",self.playListText)
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.updateName())
        self.dialog.exec()

    def updateName(self):
        state=[]
        count=0
        indexState=None
        for index in range(0,len(self.ui.dialogListBox)):
            state.append(self.ui.dialogListBox[index].isChecked())
            if state[index]==True:
                count+=1
                indexState=index
        if count>=2 :
            self.ui.dialogCheck(self.dialog2,"repeat input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog2.close())
            self.dialog2.exec()
        elif count<=0 :
            self.ui.dialogCheck(self.dialog2,"pls input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog2.close())
            self.dialog2.exec()
        elif count==1:   
            self.ui.dialogCheckEdit(self.dialog2,"update")
            self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.updateData(indexState))
            self.dialog2.exec()

    def updateData(self,number):
        listData=[self.id,self.ui.dialogText.text()]
        checkPlayListRepeat=self.db.readData("playList",["id","playList"],listData,self.db.cursor2)
        print(checkPlayListRepeat)
        if len(checkPlayListRepeat)==0:
            playList=self.ui.dialogListBox[number].text()
            data=self.db.readData("playList",["id","playList"],[self.id,playList],self.db.cursor2)
            updateData=["sequance",data[0][0]]
            self.db.updateData("playList",["playList",self.ui.dialogText.text()],updateData,self.db.cursor2,self.db.connect2)
            self.dialog2.close()
            self.dialog.close()
            self.playListSet()
        else:
            self.ui.dialogCheck(self.dialog3,"repeat")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()




    def deleteList(self):
        self.ui.dialogPlayList(self.dialog,"delete",self.playListText)
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.deleteEvent())
        self.dialog.exec()
        

    def deleteEvent(self):
        state=[]
        count=0
        indexState=None
        for index in range(0,len(self.ui.dialogListBox)):
            state.append(self.ui.dialogListBox[index].isChecked())
            if state[index]==True:
                count+=1
                indexState=index
        if count>=2 :
            self.ui.dialogCheck(self.dialog2,"repeat input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog2.close())
            self.dialog2.exec()
        elif count<=0 :
            self.ui.dialogCheck(self.dialog2,"pls input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog2.close())
            self.dialog2.exec()
        elif count==1:   
            self.ui.dialogYesNo(self.dialog2,"delete?")
            self.ui.dialogYesNoBtn[0].clicked.connect(lambda event : self.deleteData(indexState))
            self.ui.dialogYesNoBtn[1].clicked.connect(lambda event : self.dialog2.close())
            self.dialog2.exec()


    def deleteData(self,number):
        playList=self.ui.dialogListBox[number].text()
        data=self.db.readData("playList",["id","playList"],[self.id,playList],self.db.cursor2)
        deleteData=["sequance",data[0][0]]
        self.db.deleteData("playList",deleteData,self.db.cursor2,self.db.connect2)
        self.dialog2.close()
        self.dialog.close()
        self.playListSet()
            # rdData 통해서 id 랑 입력된 text 로 시퀀스 찾아서 그 시퀀스 딜리트 