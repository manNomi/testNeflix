import Video

class PlayList:
    def __init__(self,Ui):
        self.ui=Ui
        self.joinClick()

    def joinClick(self):
        for index in range(0,len(self.ui.playListBtnList)):
            self.ui.playListBtnList[index].clicked.connect(lambda event,value=index : self.joinEvent(value))

        for index in range(0,len(self.ui.mainLogoListBtn)):
           self.ui.mainLogoListBtn[index].clicked.connect(lambda event,value=index : self.move(value))

        self.ui.playListBack.clicked.connect(self.back)


    def joinEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(0)
            #Back
        else:
            pass
            #Join
    
    def move(self,number):
        self.ui.stackedWidget.setCurrentIndex(4)
        video=Video.Video(self.ui)
        
        

    def back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        
            

