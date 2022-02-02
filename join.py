class Join:
    def __init__(self,Ui):
        self.ui=Ui
        self.joinClick()

    def joinClick(self):
        for index in range(0,len(self.ui.joinBtnList)):
            self.ui.joinBtnList[index].clicked.connect(lambda event,value=index : self.joinEvent(value))

    def joinEvent(self,number):
        if number==0:
            self.ui.stackedWidget.setCurrentIndex(0)
            #Back
        else:
            pass
            #Join
        
            

