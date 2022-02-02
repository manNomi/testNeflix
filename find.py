class Find:
    def __init__(self,Ui):
        self.ui=Ui
        self.findClick()

    def findClick(self):
        for index in range(0,len(self.ui.findBtnList)):
            self.ui.findBtnList[index].clicked.connect(lambda event,value=index : self.findEvent(value))

    def findEvent(self,number):
        if number==0:
            pass
            #find PW
        elif number==1:
            pass
            #find ID
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

