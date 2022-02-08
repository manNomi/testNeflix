from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5 import *
import sys
import data
from PyQt5.QtWidgets import QApplication, QWidget
import urllib.request


class Ui:
    
    def __init__(self):
      
        self.db=data.Database()

        self.MainWindow=QtWidgets.QMainWindow()
        
        self.MainWindow.setWindowTitle("NETFLIX")
        self.MainWindow.setWindowIcon(QIcon("image/icon.png"))
        
        self.MainWindow.setGeometry(800,60,1200,900)
        self.MainWindow.setMinimumSize(1200,900)
        self.MainWindow.setMaximumSize(1200,900)
        self.MainWindow.setStyleSheet("background-color : white;")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(0,0, 1300, 1000)
        self.stackedWidget.setStyleSheet("background-color : black;")
        self.stackedWidget.setObjectName("stackedWidget")

        self.PageLogin = QtWidgets.QWidget()
        self.PageLogin.setObjectName("PageLogin")

        loginLineXY=[[480,20,370,100],[180,180,950,650]]
        self.loginLineList=[]
        for index in range(0,len(loginLineXY)):
            loginLine=QtWidgets.QLabel(self.PageLogin)
            loginLine.setGeometry(loginLineXY[index][0],loginLineXY[index][1],loginLineXY[index][2],loginLineXY[index][3])
            loginLine.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;")
            self.loginLineList.append(loginLine)
        
        loginTextXY=[[230,250,700,70],[230,480,700,70]]
        self.loginTextList=[]
        for index in range(0,len(loginTextXY)):
            loginText=QtWidgets.QLineEdit(self.PageLogin)
            if index==1:
                loginText.setEchoMode(QtWidgets.QLineEdit.Password)
            loginText.setGeometry(loginTextXY[index][0],loginTextXY[index][1],loginTextXY[index][2],loginTextXY[index][3])
            loginText.setStyleSheet("color:white;")
            font = QtGui.QFont()
            font.setFamily("Consolas")
            font.setPointSize(18)
            loginText.setFont(font)
            self.loginTextList.append(loginText) 
        
        loginLogoXY=[[20,20,200,70],[235,45,100,50],[500,30,340,80],[235,200,50,30],[235,400,140,50]]
        loginLogoText=["NETFLIX","LOGIN","Save your favorite content\nwatch it offline","ID","PASSWORD"]
        mainLogoList=[]
        for index in range(0,len(loginLogoText)):
            loginLogo=QtWidgets.QLabel(self.PageLogin)
            loginLogo.setGeometry(loginLogoXY[index][0],loginLogoXY[index][1],loginLogoXY[index][2],loginLogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            if index==0:
                font.setPointSize(40)
                loginLogo.setStyleSheet("color : red;")
            else:
                font.setPointSize(18)
                loginLogo.setStyleSheet("color : white;")
            loginLogo.setFont(font)
            loginLogo.setText(loginLogoText[index])
            mainLogoList.append(loginLogo) 

        
        loginBtnXY=[[235,660, 220, 70],[510,660,220, 70],[780,660, 220, 70]]
        loginBtnText=["Login","JOIN","FIND "]
        self.loginBtnList=[]
        for index in range(0,len(loginBtnXY)):
            loginBtn=QtWidgets.QToolButton(self.PageLogin)
            loginBtn.setGeometry(loginBtnXY[index][0],loginBtnXY[index][1],loginBtnXY[index][2],loginBtnXY[index][3])
            font = QtGui.QFont()
            loginBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            loginBtn.setFont(font)
            loginBtn.setText(loginBtnText[index])
            loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.loginBtnList.append(loginBtn)     
            
###################################################################################################
        self.PageJoin = QtWidgets.QWidget()
        self.PageJoin.setObjectName("PageJoin")

        joinLineXY=[[80,120,1050,730]]
        self.joinLineList=[]
        for index in range(0,len(joinLineXY)):
            joinLine=QtWidgets.QLabel(self.PageJoin)
            joinLine.setGeometry(joinLineXY[index][0],joinLineXY[index][1],joinLineXY[index][2],joinLineXY[index][3])
            joinLine.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;")
            self.joinLineList.append(joinLine) 
        
        joinTextXY=[]
        for index in range(0,5):
            joinTextXY.append([120,180+(140*index),600,50])
        self.joinTextList=[]
        for index in range(0,len(joinTextXY)):
            joinText=QtWidgets.QLineEdit(self.PageJoin)
            joinText.setGeometry(joinTextXY[index][0],joinTextXY[index][1],joinTextXY[index][2],joinTextXY[index][3])
            joinText.setStyleSheet("color:white;")
            font = QtGui.QFont()
            font.setFamily("Consolas")
            font.setPointSize(12)
            joinText.setFont(font)
            self.joinTextList.append(joinText) 
        
        joinLogoXY=[[20,20,200,70],[235,45,100,50],[400,45,600,50]]
        joinLogoText=["NETFLIX","JOIN","If you're not a Netflix member, please sign up"]
        mainLogoList=[]
        for index in range(0,len(joinLogoText)):
            joinLogo=QtWidgets.QLabel(self.PageJoin)
            joinLogo.setGeometry(joinLogoXY[index][0],joinLogoXY[index][1],joinLogoXY[index][2],joinLogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            if index==0:
                font.setPointSize(40)
                joinLogo.setStyleSheet("color : red;")
            else:
                font.setPointSize(18)
                joinLogo.setStyleSheet("color : white;")
            joinLogo.setFont(font)
            joinLogo.setText(joinLogoText[index])


        joinValueXY=[]
        for index in range(0,5):
            joinValueXY.append([120,130+(140*index),600,45])
        valueLogoText=["ID","PW","PW CHECK","NAME","PHONE NUMBER"]
        mainLogoList=[]
        for index in range(0,len(valueLogoText)):
            valueLogo=QtWidgets.QLabel(self.PageJoin)
            valueLogo.setGeometry(joinValueXY[index][0],joinValueXY[index][1],joinValueXY[index][2],joinValueXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            valueLogo.setStyleSheet("color : white;")
            valueLogo.setFont(font)
            valueLogo.setText(valueLogoText[index])

        joinIncorrectXY=[]
        for index in range(0,5):
            joinIncorrectXY.append([600,130+(140*index),450,45])
        self.joinCheckText=[]
        for index in range(0,5):
            IncorrectLogo=QtWidgets.QLabel(self.PageJoin)
            IncorrectLogo.setGeometry(joinIncorrectXY[index][0],joinIncorrectXY[index][1],joinIncorrectXY[index][2],joinIncorrectXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(10)
            IncorrectLogo.setStyleSheet("color : #FFC000;")
            IncorrectLogo.setFont(font)
            self.joinCheckText.append(IncorrectLogo)

        
        joinBtnXY=[[850,560, 220,80],[850,720,220,80]]
        joinBtnText=["BACK","JOIN"]
        self.joinBtnList=[]
        for index in range(0,len(joinBtnXY)):
            joinBtn=QtWidgets.QToolButton(self.PageJoin)
            joinBtn.setGeometry(joinBtnXY[index][0],joinBtnXY[index][1],joinBtnXY[index][2],joinBtnXY[index][3])
            font = QtGui.QFont()
            joinBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            joinBtn.setFont(font)
            joinBtn.setText(joinBtnText[index])
            joinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.joinBtnList.append(joinBtn)   



#############################################################################################################################

        self.PageFind = QtWidgets.QWidget()
        self.PageFind.setObjectName("PageFind")

        self.chooseIDPW = QtWidgets.QTabWidget(self.PageFind)
        self.chooseIDPW.setGeometry(50,110, 1100, 700)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setWeight(75)
        self.chooseIDPW.setFont(font)
        self.chooseIDPW.setObjectName("chooseIDPW")
        self.findID = QtWidgets.QWidget()
        self.findID.setObjectName("findID")
        self.findPW = QtWidgets.QWidget()
        self.findPW.setObjectName("findPW")
        
        findLogoXY=[[20,20,200,70],[235,45,100,50]]
        findLogoText=["NETFLIX","find"]
        for index in range(0,len(findLogoText)):
            findLogo=QtWidgets.QLabel(self.PageFind)
            findLogo.setGeometry(findLogoXY[index][0],findLogoXY[index][1],findLogoXY[index][2],findLogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            if index==0:
                font.setPointSize(40)
                findLogo.setStyleSheet("color : red;")
            else:
                font.setPointSize(18)
                findLogo.setStyleSheet("color : white;")
            findLogo.setFont(font)
            findLogo.setText(findLogoText[index])

        self.chooseIDPW.addTab(self.findPW, "")
        self.chooseIDPW.addTab(self.findID, "")
  
        self.chooseIDPW.setTabText(self.chooseIDPW.indexOf(self.findPW),"PW")
        self.chooseIDPW.setTabText(self.chooseIDPW.indexOf(self.findID),"ID")
        self.chooseIDPW.setStyleSheet("QTabBar{background-color:black; border-radius: 10px;}")
        self.stackedWidget.addWidget(self.PageFind)


        findBtnGeo=[[800, 500, 200, 70],[800, 500, 200, 70],[920, 20, 200, 70]]
        findBtnText=["find","find","BACK"]
        self.findBtnList=[]
        for index in range(0,len(findBtnGeo)):
            if index==0:
                findBtn = QtWidgets.QToolButton(self.findPW)
            elif index==1:
                findBtn = QtWidgets.QToolButton(self.findID)
            else:
                findBtn = QtWidgets.QToolButton(self.PageFind)
            findBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            findBtn.setGeometry(findBtnGeo[index][0],findBtnGeo[index][1],findBtnGeo[index][2],findBtnGeo[index][3])
            findBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setFamily("Bebas Neue")
            findBtn.setFont(font)
            findBtn.setText(findBtnText[index])
            findBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.findBtnList.append(findBtn)    

        
        self.findTextID=[]
        findValueXY=[]
        for index in range(0,2):
            Y=150+index*200
            findValueXY.append([50,Y,600,80])
        mainLogoList=[]
        for index in range(0,len(findValueXY)):
            valueLogo=QtWidgets.QLineEdit(self.findID)
            valueLogo.setGeometry(findValueXY[index][0],findValueXY[index][1],findValueXY[index][2],findValueXY[index][3])
            valueLogo.setStyleSheet("color:white")
            font = QtGui.QFont()
            font.setFamily("Consolas")
            font.setPointSize(18)
            valueLogo.setFont(font)
            self.findTextID.append(valueLogo)
        
        self.findLogoID=[]
        findLogoXY=[]
        findIDText=["Phone number","name"]
        for index in range(0,2):
            Y=100+index*200
            findLogoXY.append([50,Y,200,30])
        mainLogoList=[]
        for index in range(0,len(findLogoXY)):
            IDfindLogo=QtWidgets.QLabel(self.findID)
            IDfindLogo.setGeometry(findLogoXY[index][0],findLogoXY[index][1],findLogoXY[index][2],findLogoXY[index][3])
            IDfindLogo.setStyleSheet("color:white")
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setFamily("Bebas Neue")
            IDfindLogo.setText(findIDText[index])
            IDfindLogo.setFont(font)
            self.findLogoID.append(IDfindLogo)


        self.findTextPW=[]
        findValueXY=[]
        for index in range(0,3):
            Y=100+index*200
            findValueXY.append([50,Y,500,80])
        mainLogoList=[]
        for index in range(0,len(findValueXY)):
            valueLogoPW=QtWidgets.QLineEdit(self.findPW)
            valueLogoPW.setGeometry(findValueXY[index][0],findValueXY[index][1],findValueXY[index][2],findValueXY[index][3])
            valueLogoPW.setStyleSheet("color:white")
            font = QtGui.QFont()
            font.setFamily("Consolas")
            font.setPointSize(18)
            valueLogoPW.setFont(font)
            self.findTextPW.append(valueLogoPW)
        
        self.findLogoID=[]
        findLogoXY=[]
        findIDText=["Phone number","name","ID"]
        for index in range(0,3):
            Y=50+index*200
            findLogoXY.append([50,Y,200,30])
        mainLogoList=[]
        for index in range(0,len(findLogoXY)):
            PWfindLogo=QtWidgets.QLabel(self.findPW)
            PWfindLogo.setGeometry(findLogoXY[index][0],findLogoXY[index][1],findLogoXY[index][2],findLogoXY[index][3])
            PWfindLogo.setStyleSheet("color:white")
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setFamily("Bebas Neue")
            PWfindLogo.setText(findIDText[index])
            PWfindLogo.setFont(font)
            self.findLogoID.append(PWfindLogo)
#################################################################################################################
        self.PageplayList = QtWidgets.QWidget()
        self.PageplayList.setObjectName("PageplayList")

        playListLogoXY=[[20,20,200,70],[235,45,100,50]]
        playListLogoText=["NETFLIX","playList"]
        mainLogoList=[]
        for index in range(0,len(playListLogoText)):
            playListLogo=QtWidgets.QLabel(self.PageplayList)
            playListLogo.setGeometry(playListLogoXY[index][0],playListLogoXY[index][1],playListLogoXY[index][2],playListLogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            if index==0:
                font.setPointSize(40)
                playListLogo.setStyleSheet("color : red;")
            else:
                font.setPointSize(18)
                playListLogo.setStyleSheet("color : white;")
            playListLogo.setFont(font)
            playListLogo.setText(playListLogoText[index])


        

##############
     
        self.scrollArea = QtWidgets.QScrollArea(self.PageplayList)
        self.scrollArea.setGeometry(80,150,1050,730)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(0, 10, 181, 81)
        self.groupBox.setObjectName("groupBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(20, 20, 980,680)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.groupBox.setLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.groupBox)
        

        valueLogoText=[]
        image2=['image/image1.PNG','image/image2.PNG','image/image3.PNG','image/image4.PNG','image/image5.PNG']
        self.mainLogoListBtn=[]
        self.qPixmapVar = QPixmap() 
        count=0
        for index in range(0,len(valueLogoText)):
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            valueLogo=QtWidgets.QToolButton(self.verticalLayoutWidget)
            valueLogo.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;border-image:url("+image2[0]+")")
            valueLogo.setFont(font)
            valueLogo.setText(valueLogoText[index])
            valueLogo.setFixedWidth(484)
            valueLogo.setFixedHeight(270)
            valueLogo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            if (index+2)%2==0:
                self.verticalLayout.setWidget(count,QtWidgets.QFormLayout.LabelRole,valueLogo)
            else:
                self.verticalLayout.setWidget(count,QtWidgets.QFormLayout.FieldRole,valueLogo)
                count+=1
            self.mainLogoListBtn.append(valueLogo)
        
#####################        

        self.playListBack=QtWidgets.QToolButton(self.PageplayList)
        self.playListBack.setGeometry(850,50,220,80)
        font = QtGui.QFont()
        self.playListBack.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.playListBack.setFont(font)
        self.playListBack.setText("BACK")
        self.playListBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        playListBtnXY=[]
        for index in range (0,4):
            playListBtnXY.append([250+130*index,100,100,40])
        playListBtnText=["search","update","insert","delete"]
        self.playListBtnList=[]
        for index in range(0,len(playListBtnXY)):
            playListBtn=QtWidgets.QToolButton(self.PageplayList)
            playListBtn.setGeometry(playListBtnXY[index][0],playListBtnXY[index][1],playListBtnXY[index][2],playListBtnXY[index][3])
            font = QtGui.QFont()
            playListBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            playListBtn.setFont(font)
            playListBtn.setText(playListBtnText[index])
            playListBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.playListBtnList.append(playListBtn)

#####################################################################################################################
        self.PageVideo = QtWidgets.QWidget()
        self.PageVideo.setObjectName("playVideo")

        playVideoLogoXY=[[20,20,200,70],[235,45,100,50]]
        playVideoLogoText=["NETFLIX","Video"]
        mainLogoList=[]
        for index in range(0,len(playVideoLogoText)):
            playVideoLogo=QtWidgets.QLabel(self.PageVideo)
            playVideoLogo.setGeometry(playVideoLogoXY[index][0],playVideoLogoXY[index][1],playVideoLogoXY[index][2],playVideoLogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            if index==0:
                font.setPointSize(40)
                playVideoLogo.setStyleSheet("color : red;")
            else:
                font.setPointSize(18)
                playVideoLogo.setStyleSheet("color : white;")
            playVideoLogo.setFont(font)
            playVideoLogo.setText(playVideoLogoText[index])

        self.scrollArea2 = QtWidgets.QScrollArea(self.PageVideo)
        self.scrollArea2.setGeometry(900,180,200,600)
        self.scrollArea2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea2")
        
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(0, 0, 188, 119)
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")

        self.groupBox2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents2)
        self.groupBox2.setGeometry(0, 10, 181, 81)
        self.groupBox2.setObjectName("groupBox2")

        self.verticalLayoutVideoWidget = QtWidgets.QWidget(self.groupBox2)
        self.verticalLayoutVideoWidget.setGeometry(20, 20, 980,680)
        self.verticalLayoutVideoWidget.setObjectName("verticalLayoutVideoWidget")

        self.verticalLayoutVideo = QtWidgets.QFormLayout(self.verticalLayoutVideoWidget)
        self.verticalLayoutVideo.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutVideo.setObjectName("verticalLayoutVideo")
        self.verticalLayoutVideo.setSpacing(10)
        self.verticalLayoutVideo.setVerticalSpacing(100)

        self.groupBox2.setLayout(self.verticalLayoutVideo)
        self.scrollArea2.setWidget(self.groupBox2)

        valueLogoText2=[]
        image2=['image/image1.PNG','image/image2.PNG','image/image3.PNG','image/image4.PNG','image/image5.PNG']
        self.videoListBtn=[]
        self.qPixmapVar = QPixmap() 
        count=0
        for index in range(0,len(valueLogoText2)):
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            valueLogo2=QtWidgets.QToolButton(self.verticalLayoutVideoWidget)
            valueLogo2.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;border-image:url("+image2[index]+")")
            valueLogo2.setFont(font)
            valueLogo2.setText(valueLogoText2[index])
            valueLogo2.setFixedWidth(162)
            valueLogo2.setFixedHeight(90)
            valueLogo2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.verticalLayoutVideo.setWidget(count,QtWidgets.QFormLayout.LabelRole,valueLogo2)
            self.videoListBtn.append(valueLogo2)
            count+=1
        
        self.videoBack=QtWidgets.QToolButton(self.PageVideo)
        self.videoBack.setGeometry(850,50,220,80)
        font = QtGui.QFont()
        self.videoBack.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.videoBack.setFont(font)
        self.videoBack.setText("BACK")
        self.videoBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.videoPlay=QtWidgets.QFrame(self.PageVideo)
        self.videoPlay.setGeometry(130,180,720,540)
        self.videoPlay.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
        
  

        self.videoName=QtWidgets.QLabel(self.PageVideo)
        self.videoName.setGeometry(130,750,570,80)
        font = QtGui.QFont()
        self.videoName.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
        font.setFamily("Bebas Neue")
        font.setPointSize(10)
        self.videoName.setFont(font)
        self.videoName.setText("videoName")

        self.videoBtns=[]
        videoBtnText=["▶","■","〓"]
        for index in range(0,len(videoBtnText)):
            videoBtn=QtWidgets.QToolButton(self.PageVideo)
            videoBtn.setGeometry(700+(50*index),750,50,80)
            font = QtGui.QFont()
            videoBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            font.setPointSize(18)
            videoBtn.setFont(font)
            videoBtn.setText(videoBtnText[index])
            videoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.videoBtns.append(videoBtn)



        self.horizontalSlider = QtWidgets.QSlider(self.PageVideo)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setGeometry(920, 800, 160, 22)
        self.horizontalSlider.setStyleSheet("background-color:black")
        self.horizontalSlider.setObjectName("horizontalSlider")

       

        self.videoDeleteBtn=QtWidgets.QToolButton(self.PageVideo)
        self.videoDeleteBtn.setGeometry(250+390,100,100,40)
        font = QtGui.QFont()
        self.videoDeleteBtn.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.videoDeleteBtn.setFont(font)
        self.videoDeleteBtn.setText("delete")
        self.videoDeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


#############################################################################################################
        self.PageLoading = QtWidgets.QWidget()
        self.PageLoading.setObjectName("PageLoading")
        self.loadingLogo=QtWidgets.QLabel(self.PageLoading)
        self.loadingLogo.setGeometry(100,0,1200,900)
        self.loadingLogo.setStyleSheet("background-color:black")



###############################################################################################################

        self.PageDownloading = QtWidgets.QWidget()
        self.PageDownloading.setObjectName("PageDownloading")
        self.DownloadingLogo=QtWidgets.QLabel(self.PageDownloading)
        self.DownloadingLogo.setGeometry(100,0,1200,900)
        self.DownloadingLogo.setStyleSheet("background-color:white")
        self.logoDown=QtWidgets.QLabel(self.PageDownloading)
       


###############################################################################################################

        self.stackedWidget.addWidget(self.PageLogin)
        self.stackedWidget.addWidget(self.PageJoin)
        self.stackedWidget.addWidget(self.PageFind)
        self.stackedWidget.addWidget(self.PageplayList)
        self.stackedWidget.addWidget(self.PageVideo)
        self.stackedWidget.addWidget(self.PageLoading)
        self.stackedWidget.addWidget(self.DownloadingLogo)



        self.stackedWidget.setCurrentIndex(6)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.show()



    def dialogCheck(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 333)
        Dialog.setStyleSheet("background-color : black;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        self.dialogLabel.setText(text)

        self.dialogCheckbtn=QtWidgets.QToolButton(Dialog)
        self.dialogCheckbtn.setGeometry(215,200,120,60)
        font = QtGui.QFont()
        self.dialogCheckbtn.setStyleSheet("background-color: red;color:white")
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogCheckbtn.setFont(font)
        self.dialogCheckbtn.setText("check")
        self.dialogCheckbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def dialogYesNo(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 333)
        Dialog.setStyleSheet("background-color : black;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        self.dialogLabel.setText(text)
        self.dialogYesNoBtn=[]
        dialogText=["yes","no"]
        for index in range(0,2):
            dialogYesNoBtn=QtWidgets.QToolButton(Dialog)
            dialogYesNoBtn.setGeometry(155+index*120,200,120,60)
            font = QtGui.QFont()
            dialogYesNoBtn.setStyleSheet("background-color: red;color:white")
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            dialogYesNoBtn.setFont(font)
            dialogYesNoBtn.setText(dialogText[index])
            dialogYesNoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.dialogYesNoBtn.append(dialogYesNoBtn)

    def dialogPlayList(self,Dialog,text,List):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200,900)
        Dialog.setStyleSheet("background-color : black;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(25, 30, 100, 50)
        
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : white;")
        self.dialogLabel.setObjectName("label")
        self.dialogLabel.setText("playlist")

        scrollArea = QtWidgets.QScrollArea(Dialog)
        scrollArea.setGeometry(100,150,900,600)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea3")

        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(0, 0, 188, 119)
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents2")

        groupBox = QtWidgets.QGroupBox(scrollAreaWidgetContents)
        groupBox.setGeometry(0, 10, 181, 81)
        groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(groupBox)
        self.verticalLayoutWidget.setGeometry(20, 20, 980,680)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        verticalLayout.setVerticalSpacing(100)
        groupBox.setLayout(verticalLayout)
        scrollArea.setWidget(groupBox)

        valueLogoText=List
        self.dialogListBox=[]
        count=0
        for index in range(0,len(valueLogoText)):
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            value=QtWidgets.QCheckBox(self.verticalLayoutWidget)
            value.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")
            value.setFont(font)
            value.setText(valueLogoText[index])
            value.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            verticalLayout.setWidget(count,QtWidgets.QFormLayout.LabelRole,value)
            self.dialogListBox.append(value)
            count+=1

        btnText=[text,"back"]
        self.Listcheckbtn=[]
        for index in range(0,len(btnText)):
            isertCheckbtn=QtWidgets.QToolButton(Dialog)
            isertCheckbtn.setGeometry(1040,700-(index*200),120,60)
            font = QtGui.QFont()
            isertCheckbtn.setStyleSheet("background-color: red;color:white")
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            isertCheckbtn.setFont(font)
            isertCheckbtn.setText(btnText[index])
            isertCheckbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            QtCore.QMetaObject.connectSlotsByName(Dialog)
            self.Listcheckbtn.append(isertCheckbtn)

    def dialogCheckEdit(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 333)
        Dialog.setStyleSheet("background-color : black;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(80, -50, 600, 300)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        self.dialogLabel.setText(text)

        self.dialogText = QtWidgets.QLineEdit(Dialog)
        self.dialogText.setGeometry(80, 150, 400, 50)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.dialogText.setFont(font)
        self.dialogText.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
        self.dialogText.setObjectName("label")
 
        self.dialogCheckEditBtn=QtWidgets.QToolButton(Dialog)
        self.dialogCheckEditBtn.setGeometry(215,280,120,60)
        font = QtGui.QFont()
        self.dialogCheckEditBtn.setStyleSheet("background-color: red;color:white")
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.dialogCheckEditBtn.setFont(font)
        self.dialogCheckEditBtn.setText("check")
        self.dialogCheckEditBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# self.ui.dialog(self.Dialog,"Congratulations. You succeeded in signing up")
#             self.Dialog.show()




    def playList(self,playlistData):


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(0, 10, 181, 81)
        self.groupBox.setObjectName("groupBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(20, 20, 980,680)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.groupBox.setLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.groupBox)


        valueLogoText=playlistData

        image2=['image/image1.PNG','image/image2.PNG','image/image3.PNG','image/image4.PNG','image/image5.PNG']
        self.mainLogoListBtn=[]
        self.qPixmapVar = QPixmap()
        count=0
        self.mainLogoListBtn.clear()
        
        print(self.mainLogoListBtn)
        print("값:"+str(playlistData))
        for index in range(0,len(valueLogoText)):
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(18)
            valueLogo=QtWidgets.QToolButton(self.verticalLayoutWidget)
            valueLogo.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
            valueLogo.setFont(font)
            valueLogo.setText(valueLogoText[index])
            valueLogo.setFixedWidth(484)
            valueLogo.setFixedHeight(270)
            valueLogo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            if (index+2)%2==0:
                self.verticalLayout.setWidget(count,QtWidgets.QFormLayout.LabelRole,valueLogo)
            else:
                self.verticalLayout.setWidget(count,QtWidgets.QFormLayout.FieldRole,valueLogo)
                count+=1
            self.mainLogoListBtn.append(valueLogo)
        print(self.mainLogoListBtn)

    def playVideoSet(self,playlistData):
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(0, 0, 188, 119)
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")

        self.groupBox2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents2)
        self.groupBox2.setGeometry(0, 10, 181, 81)
        self.groupBox2.setObjectName("groupBox2")

        self.verticalLayoutVideoWidget2 = QtWidgets.QWidget(self.groupBox2)
        self.verticalLayoutVideoWidget2.setGeometry(20, 20, 980,680)
        self.verticalLayoutVideoWidget2.setObjectName("verticalLayoutVideoWidget2")

        self.verticalLayoutVideo2 = QtWidgets.QFormLayout(self.verticalLayoutVideoWidget2)
        self.verticalLayoutVideo2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutVideo2.setObjectName("verticalLayoutVideo2")
        self.verticalLayoutVideo2.setSpacing(10)
        self.verticalLayoutVideo2.setVerticalSpacing(100)

        self.groupBox2.setLayout(self.verticalLayoutVideo2)
        self.scrollArea2.setWidget(self.groupBox2)

        valueLogoText2=playlistData

        self.videoListBtn=[]

        self.videoListBtn.clear()
        print("값:"+str(playlistData))
        print(len(valueLogoText2))
        for index in range(0,len(valueLogoText2)):
            font = QtGui.QFont()
            font.setFamily("Bebas Neue")
            font.setPointSize(9)
            valueLogo2=QtWidgets.QToolButton(self.verticalLayoutVideoWidget2)
            urlString = valueLogoText2[index][1]
            imageFromWeb = urllib.request.urlopen(urlString).read()
            qPixmapVar = QPixmap()
            qPixmapVar.loadFromData(imageFromWeb)
            qPixmapVar=qPixmapVar.scaled(162, 90)
            icon = QIcon() # QIcon 생성
            icon.addPixmap(qPixmapVar)
            valueLogo2.setIcon(icon)
            valueLogo2.setIconSize(QtCore.QSize(162, 90))
            valueLogo2.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
            valueLogo2.setFont(font)
            valueLogo2.setText(valueLogoText2[index][0])
            valueLogo2.setFixedWidth(162)
            valueLogo2.setFixedHeight(90)
            valueLogo2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.verticalLayoutVideo2.addWidget(valueLogo2)

            self.videoListBtn.append(valueLogo2)




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Ui()

    dialog=QtWidgets.QDialog()
    Main.dialogCheckEdit(dialog,"Do you really want to delete it?")
    dialog.show()

    sys.exit(app.exec_())
    
