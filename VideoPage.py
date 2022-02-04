class Video:
    def __init__(self,Ui,id):
        self.ui=Ui
        self.id=id
        self.videoClick()
        self.playListSet()

    def videoClick(self):
        for index in range(0,len(self.ui.joinBtnList)):
            self.ui.videoBtn[index].clicked.connect(lambda event,value=index : self.videoEvent(value))

        self.ui.videoBack.clicked.connect(self.back)

    def videoEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(0)
            #Back
        else:
            pass
            #Join

    def back(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def playListSet(self):
        listData=self.db.readData("playList",["id"],[self.id],self.db.cursor2)
        self.playListText=[]
        for index in range (0,len(listData)):
            self.playListText.append(listData[index][2])
        self.ui.playList(self.playListText)

#영상재생 thread는 video에서 할것 