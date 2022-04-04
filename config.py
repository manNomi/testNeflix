from PyQt5 import QtWidgets

class Config:
    def __init__(self,ui):
        self.ui=ui
        # self.dialog=QtWidgets.QDialog()     #dialog check
        # self.dialog2=QtWidgets.QDialog()    #dialogPlayList
        # self.dialog3=QtWidgets.QDialog()    # dialog check Edit
        # self.dialog4=QtWidgets.QDialog()

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
