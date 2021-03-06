import data
import vlc
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import time

class Video:
    def __init__(self,Ui):
        self.dialog=QtWidgets.QDialog()
        self.dialog2=QtWidgets.QDialog()
        self.dialog4=QtWidgets.QDialog()

        self.db=data.Database()
        
        self.ui=Ui
        self.play=PlayVideo(self.ui)
        self.id=None
        self.playList=None
        
        self.videoListSet()
        
        self.ui.horizontalSlider.valueChanged.connect(self.volumeEvent)

        self.ui.videoDeleteBtn.clicked.connect(self.deleteList)

        self.sec=0
       



    def videoClick(self):
        for index in range(0,len(self.ui.videoBtns)):
            self.ui.videoBtns[index].clicked.connect(lambda event,value=index : self.play.btnEvent(value))
        self.ui.videoBack.clicked.connect(self.back)
        
        for index in range(0,len(self.ui.videoListBtn)):
            self.ui.videoListBtn[index].clicked.connect(lambda event,value=index : self.videoPlay(value))
            
        
    

    def deleteList(self):
        videoList=[]
        for index in range(0,len(self.playVideoText)):
            videoList.append(self.playVideoText[index][0])
        print("비디오 리스트는 :"+str(videoList))
        
        self.ui.dialogPlayList(self.dialog,"delete",videoList)
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
            self.ui.dialogYesNo(self.dialog4,"delete?")
            self.ui.dialogYesNoBtn[0].clicked.connect(lambda event : self.deleteData(indexState))
            self.ui.dialogYesNoBtn[1].clicked.connect(lambda event : self.dialog4.close())
            self.dialog4.exec()


    def deleteData(self,number):
        video=self.ui.dialogListBox[number].text()
        data=self.db.readData("playVideo",["id","playList","video"],[self.id,self.playList,video],self.db.cursor3)
        deleteData=["sequance",data[0][0]]
        self.db.deleteData("playVideo",deleteData,self.db.cursor3,self.db.connect3)
        self.dialog.close()
        self.dialog4.close()
        self.videoListSet()

    def volumeEvent(self):
        self.play.setVolume(self.ui.horizontalSlider.value())


    def back(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.play.playEvent()

       
    def videoListSet(self):
        listData=self.db.readData("playVideo",["id","playList"],[self.id,self.playList],self.db.cursor3)
        self.playVideoText=[]
        for index in range (0,len(listData)):
            self.playVideoText.append([listData[index][3],listData[index][5]])
        self.ui.playVideoSet(self.playVideoText)
        self.videoClick()
    



    def videoPlay(self,num):
        self.play.playEvent()
        listData=self.db.readData("playVideo",["id","playList"],[self.id,self.playList],self.db.cursor3)
        print("listData="+str(listData))
        self.play.setVideoPlay(listData,num)


    

class PlayVideo:
    def __init__(self,ui):
        self.ui=ui
        self.instance = vlc.Instance()
    
    def btnEvent(self,num):
        self.play.PlayPause(num)
        if num==0:
            self.timer.timeRestart()
        elif num==1:
            self.ui.videoName.setText("")
            self.timer.timerSet()
        else :
            self.timer.timerStop()

    def playEvent(self):
        try:
            self.play.playStop()
            self.ui.videoName.setText("")
            self.timer.timerSet()
        except:
            pass

    def setVolume(self, Volume):
        self.play.changeVolume(Volume)

    def setVideoPlay(self,listData,num):
        try:
            self.sec=listData[num][4]
            self.mp = self.instance.media_player_new()
            self.mp.set_hwnd(int(self.ui.videoPlay.winId()))
            print(self.ui.videoPlay.winId())
            mf="videos/"+str(listData[num][3])+".mp4"
            self.ui.videoName.setText(str(listData[num][3]))
            media = self.instance.media_new(mf)
            media.get_mrl()
            self.mp.set_media(media)
            self.play=Play(self.mp)
            self.play.start()
            
            self.progressbarSet(listData[num][4])
           
        except:
            self.ui.videoName.setText("LOADING....")

    def progressBarEvnet(self,num):
        self.ui.horizontalSlider2.setValue(num);
      
    
    def progressbarSet(self,time):
        self.timer=Timer(time)
        self.ui.horizontalSlider2.setMaximum(time)
        self.ui.horizontalSlider2.setValue(0);
        self.timer.time.connect(self.progressBarEvnet)
        self.timer.start()


class Play(QThread):
    playvideo = pyqtSignal(int)  

    def __init__(self,play):
        super().__init__()
        self.playVideo=play
        self.timer=0
        
    def changeVolume(self, Volume):
        self.playVideo.audio_set_volume(100-Volume)

    def run(self):
        print("시작")
        self.playVideo.play()
        
    def playStop(self):
        self.playVideo.stop()
        
    def PlayPause(self,num):
        if num==0:
            if self.playVideo.is_playing()==False:
                self.playVideo.play()
        elif num==1:
            self.playVideo.stop()
        else:
            if self.playVideo.is_playing():
                self.playVideo.pause()

    
class Timer(QThread):
    time = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self,sec):
        super().__init__()
        self.total=sec
        self.timer=0
        self.timerCheck=True
        self.timeStop=False
    def run(self):
        while self.timerCheck:
            if self.timeStop!=True:
                self.time.emit(self.timer)
                time.sleep(1)
                self.timer+=1
            if self.total<=self.timer:
                self.timerCheck=False
        
    def timerSet(self): # 이름 init 과 같은 이름이 좀더 어울린다 수정 
        self.timerCheck=False
        self.timer=0

    def timerStop(self):
       self.timeStop=True
    
    def timeRestart(self):
       self.timeStop=False

        
