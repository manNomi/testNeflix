from json import load
from itsdangerous import exc
import VideoPage
from PyQt5 import QtWidgets
import data
import loadingPage
import pafy
import videoLoading
import urllib.request
from PyQt5.QtGui import *

class PlayList:
    def __init__(self,Ui,con):
        self.ui=Ui
        self.con=con
        self.load=loadingPage.Loading(self.ui)
        self.Videoload=videoLoading.LoadingVideo(self.ui)
        self.video=VideoPage.Video(self.ui)
        self.db=data.Database()
        self.dialog=QtWidgets.QDialog()     # dialog check edit
        self.dialog2=QtWidgets.QDialog()    # dialogPlayList
        self.dialog3=QtWidgets.QDialog()    # dialog check 
        self.dialog4=QtWidgets.QDialog()    # dialogYesNo
        self.id=None
        self.playListText=[]
        self.playList=[]
        self.playListClick()
        self.playListbtnEvent()


    def playListbtnEvent(self):
        self.ui.playListBack.clicked.connect(self.backEvent)
        for index in range(0,len(self.ui.playListBtnList)):
            self.ui.playListBtnList[index].clicked.connect(lambda event,value=index : self.playListEvent(value))
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
            self.ui.dialogCheckEdit(self.dialog,"insert")
            self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.insertPlayList())
            self.dialog.exec()
        else:
            self.deleteList()

    def insertPlayList(self):
        listData=[self.id,self.ui.dialogText.text()]
        checkPlayListRepeat=self.db.readData("playList",["id","playList"],listData,self.db.cursor2)
        print(len(checkPlayListRepeat))
        if len(checkPlayListRepeat)==0:
            self.db.insertData("playList",self.db.column2Value,listData,self.db.cursor2,self.db.connect2)
            self.dialog.close()
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

        self.videoListText=[]
        for index in range(0,len(listData)):
            listData2=self.db.readData("playVideo",["id","playList"],[self.id,self.playListText[index]],self.db.cursor3)
            try:
                self.videoListText.append(listData2[0][3])
            except:
                self.videoListText.append("")
        print("비디오제목은:"+str(self.videoListText))
        self.ui.playList(self.playListText,self.videoListText)
        self.playListClick()
        

       


    def moveEvent(self,number):
        self.load.setMovie(4)
        self.video.id=self.id
        self.video.playList=self.playListText[number]
        self.video.videoPlay(0)
        self.presentList=self.playListText[number]
        self.video.videoListSet()
  



    def backEvent(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.con.setTextClear()

    def updateList(self):
        self.ui.dialogPlayList(self.dialog2,"update",self.playListText)
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog2.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.updateName())
        self.dialog2.exec()


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
            self.ui.dialogCheck(self.dialog3,"repeat input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count<=0 :
            self.ui.dialogCheck(self.dialog3,"pls input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count==1:   
            self.ui.dialogCheckEdit(self.dialog,"update")
            self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.updateData(indexState))
            self.dialog.exec()


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
        self.ui.dialogPlayList(self.dialog2,"delete",self.playListText)
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog2.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.deleteEvent())
        self.dialog2.exec()

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
            self.ui.dialogCheck(self.dialog3,"repeat input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count<=0 :
            self.ui.dialogCheck(self.dialog3,"pls input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count==1:   
            self.ui.dialogYesNo(self.dialog4,"delete?")
            self.ui.dialogYesNoBtn[0].clicked.connect(lambda event : self.deleteData(indexState))
            self.ui.dialogYesNoBtn[1].clicked.connect(lambda event : self.dialog4.close())
            self.dialog4.exec()


    def deleteData(self,number):
        playList=self.ui.dialogListBox[number].text()
        data=self.db.readData("playList",["id","playList"],[self.id,playList],self.db.cursor2)
        deleteData=["sequance",data[0][0]]
        data=self.db.readData("playVideo",["id","playList"],[self.id,playList],self.db.cursor3)
        try:
            deleteData2=["sequance",data[0][0]]
            self.db.deleteData("playList",deleteData,self.db.cursor2,self.db.connect2)
            self.db.deleteData("playVideo",deleteData2,self.db.cursor3,self.db.connect3)
            self.dialog4.close()
            self.dialog2.close()
            self.playListClick()
            self.playListSet()
        except:
            self.db.deleteData("playList",deleteData,self.db.cursor2,self.db.connect2)
            self.dialog4.close()
            self.dialog2.close()
            self.playListClick()
            self.playListSet()


        

            # rdData 통해서 id 랑 입력된 text 로 시퀀스 찾아서 그 시퀀스 딜리트 


    def searchList(self):
        self.ui.dialogPlayList(self.dialog2,"search",self.playListText)
        self.ui.Listcheckbtn[1].clicked.connect(lambda event : self.dialog2.close())
        self.ui.Listcheckbtn[0].clicked.connect(lambda event : self.videoInsertEvent())
        self.dialog2.exec()


    def insertVideo(self,number):
        playList=self.ui.dialogListBox[number].text()
        videoData=self.storeVideo(self.ui.dialogText.text())
        try:
            listData=[self.id,playList,videoData[0],videoData[1],videoData[2]]
            print(listData)
            checkPlayListRepeat=self.db.readData("playVideo",["id","playList","video","time","imageURL"],listData,self.db.cursor3)
            print(len(checkPlayListRepeat))
            if len(checkPlayListRepeat)==0:
                self.dialog2.close()
                self.dialog.close()
                self.presentList=playList
                self.db.insertData("playVideo",self.db.column3Value,listData,self.db.cursor3,self.db.connect3)
                self.playListClick()
                qPixmapVar = QPixmap()
                urlString = videoData[2]
                imageFromWeb = urllib.request.urlopen(urlString).read()
                qPixmapVar.loadFromData(imageFromWeb)
                qPixmapVar=qPixmapVar.scaled(480,270)
                qPixmapVar.save("thumbnail/"+videoData[0]+".PNG")
                self.Videoload.setDown(self.best)
                self.playListSet()
            else:
                self.ui.dialogCheck(self.dialog3,"repeat")
                self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
                self.dialog3.exec()
        except:
            self.ui.dialogCheck(self.dialog3,"URL wrong")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()

    def videoInsertEvent(self):
        state=[]
        count=0
        indexState=None
        for index in range(0,len(self.ui.dialogListBox)):
            state.append(self.ui.dialogListBox[index].isChecked())
            if state[index]==True:
                count+=1
                indexState=index
        if count>=2 :
            self.ui.dialogCheck(self.dialog3,"repeat input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count<=0 :
            self.ui.dialogCheck(self.dialog3,"pls input")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()
        elif count==1:   
            self.ui.dialogCheckEdit(self.dialog,"Insert Video")
            self.ui.dialogCheckEditBtn.clicked.connect(lambda event : self.insertVideo(indexState))
            self.dialog.exec()

    


    def storeVideo(self,url):
        try:
            video = pafy.new(url)
            streams = video.streams
            for i in streams:
                print(i)
            # get best resolution regardless of format
            self.best = video.getbest()
            print(self.best.resolution, self.best.extension)
            # Download the video

            sec=int(video.duration[0])*36000+int(video.duration[1])*3600+int(video.duration[3])*600+int(video.duration[4])*60+int(video.duration[6])*10+int(video.duration[7])
            videoName=video.title
            videoImage = video.bigthumb

            return videoName,sec,videoImage
        except:
            self.ui.dialogCheck(self.dialog3,"URL wrong")
            self.ui.dialogCheckbtn.clicked.connect(lambda event : self.dialog3.close())
            self.dialog3.exec()