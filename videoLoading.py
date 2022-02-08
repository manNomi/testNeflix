from PyQt5.QtCore import *
import os

class LoadingVideo:
    def __init__(self,ui):
        self.ui=ui
    def setDown(self,downLoad):
        self.downLoad=downLoad
        self.timer =Download(self.downLoad)
        self.timer.start()


class Download(QThread):
    time = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self,download):
        super().__init__()
        self.down=download
    def run(self):
        filename =self.down.download(filepath="videos/")
        BASE_DIR = os.getcwd() + "\\" + "download"
        print(BASE_DIR)
            
