import data
class Video:
    def __init__(self,Ui,id,playList):
        self.db=data.Database()
        self.ui=Ui
        self.id=id
        self.playList=playList
        self.videoClick()
        self.playListSet()


    def videoClick(self):
        for index in range(0,len(self.ui.videoBtn)):
            self.ui.videoBtn[index].clicked.connect(lambda event,value=index : self.videoEvent(value))
        self.ui.videoBack.clicked.connect(self.back)

    def videoEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            pass
            

    def back(self):
        self.ui.stackedWidget.setCurrentIndex(3)
       
    def playListSet(self):
        listData=self.db.readData("playVideo",["id","playList"],[self.id,self.playList],self.db.cursor3)
        self.playListText=[]
        for index in range (0,len(listData)):
            self.playListText.append(listData[index][3])
        self.ui.playVideoSet(self.playListText)
        self.videoClick()

#영상재생 thread는 video에서 할것 