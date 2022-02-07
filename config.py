
class Config:
    def __init__(self,ui):
        self.ui=ui
    def setTextClear(self):
        for index in range (0,len(self.ui.joinCheckText)):
            self.ui.joinCheckText[index].clear()
        for index in range (0,len(self.ui.joinTextList)):
            self.ui.joinTextList[index].clear()
        for index in range(0,len(self.ui.findTextPW)):
            self.ui.findTextPW[index].clear()
        for index in range(0,len(self.ui.findTextID)):
            self.ui.findTextID[index].clear()
        for index in range(0,len(self.ui.loginTextList)):
            self.ui.loginTextList[index].clear()
