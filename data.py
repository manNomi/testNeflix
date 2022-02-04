import sqlite3 
# pk 무조건 존재해야한다 -> 유일한 값이기 때문 
#----------------------------------------------------------------------------------------#
class Database:
    def __init__(self):
        self.connect1=None
        self.connect2=None
        self.connect3=None

        self.cursor1=None  
        self.cursor2=None  
        self.cursor3=None    

        self.connect1=sqlite3.connect("src\curd.db")
        self.connect2=sqlite3.connect("src\playList.db")
        self.connect3=sqlite3.connect("src\ video.db")

        self.column1=['sequance','id','pw','Name','phone']
        self.column1Value=['id','pw','Name','phone']
        self.row1=['INTEGER PRIMARY KEY','TEXT','TEXT','TEXT','TEXT']

        self.column2=['sequance','id','playList']
        self.column2Value=['id','playList']
        self.row2=['INTEGER PRIMARY KEY','TEXT','TEXT']

        self.column3=['sequance','id','video']
        self.column3Value=['id','video']
        self.row3=['INTEGER PRIMARY KEY','TEXT','TEXT']


        self.cursor1=self.connect1.cursor()
        self.cursor2=self.connect2.cursor()
        self.cursor3=self.connect2.cursor()

        self.create("user",self.column1,self.row1,self.cursor1)
        self.create("playList",self.column2,self.row2,self.cursor2)
        self.create("video",self.column2,self.row2,self.cursor3)

#----------------------------------------------------------------------------------------#
    def create(self,user,column,row,cursor):
        table=[column,row]
        sql="CREATE TABLE IF NOT EXISTS "
        sql+=user+"("
        for index in range(0,len(column)):
            if index!=0:
                print(" ",end="")
            sql+=str(table[0][index])+" "+str(table[1][index])
            if index!=len(column)-1:
                sql+=","
        sql+=");"
        print(sql)
        cursor.execute(sql)
#----------------------------------------------------------------------------------------#
    def insertData(self,table,colums,values,cursor,connect):  
        userData=[colums,values]
        sql="INSERT INTO "+table+"("
        for index in range(0,len(userData[0])):
            sql+="'"+str(userData[0][index])+"'"
            if index!=len(userData[0])-1:
                sql+=","
        sql+=")VALUES("
        for index in range(0,len(userData[1])):
            sql+="'"+str(userData[1][index])+"'"
            if index!=len(userData[1])-1:
                sql+=","
        sql+=");"
        print(sql)
        cursor.execute(sql)
        connect.commit()
#----------------------------------------------------------------------------------------#
    def deleteData(self,table,sequance,cursor,connect): 
        sql="DELETE FROM "
        sql+=table+" WHERE "+sequance[0]+"="+str(sequance[1])+";"
        print(sql)
        cursor.execute(sql)
        connect.commit()
#----------------------------------------------------------------------------------------#
    def updateData(self,table,pw,sequance,cursor):
        value=pw
        sql="UPDATE "
        sql+=table+" SET "+""
        sql+=str(value[0])+"="+str(value[1])
        sql+=" WHERE "+sequance[0]+"="+str(sequance[1])
        sql+=";"
        print(sql)
        cursor.execute(sql)
        self.connect.commit()
#----------------------------------------------------------------------------------------#
    def readData(self,table,colums,values,cursor):  
        userData=[colums,values]
        sql="SELECT *FROM "+table+ " WHERE "
        for index in range(0,len(userData[0])):
            if index!=0:
                sql+=" AND "
            sql+=str(userData[0][index])+"="+"'"+str(userData[1][index])+"'"
        sql+=";"
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        return result
#----------------------------------------------------------------------------------------#