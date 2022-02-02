import sqlite3 
# pk 무조건 존재해야한다 -> 유일한 값이기 때문 
#----------------------------------------------------------------------------------------#
class Database:
    def __init__(self):
        self.connect=None
        self.cursor=None    
        self.connect=sqlite3.connect("src\curd.db")
        self.column=['sequance','id','pw','Nickname','phone','birth','gender']
        self.row=['INTEGER PRIMARY KEY','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT']
        self.cursor=self.connect.cursor()
        self.rows=["id", "pw","Nickname","phone","birth","gender"]
        self.create()
#----------------------------------------------------------------------------------------#
    def create(self):
        table=[self.column,self.row]
        sql="CREATE TABLE IF NOT EXISTS"
        sql+=" user("
        for index in range(0,len(self.column)):
            if index!=0:
                print(" ",end="")
            sql+=str(table[0][index])+" "+str(table[1][index])
            if index!=len(self.column)-1:
                sql+=","
        sql+=");"
        print(sql)
        self.cursor.execute(sql)
#----------------------------------------------------------------------------------------#
    def insertData(self,table,colums,values):  
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
        self.cursor.execute(sql)
        self.connect.commit()
#----------------------------------------------------------------------------------------#
    def deleteData(self,table,sequance): 
        sql="DELETE FROM "
        sql+=table+" WHERE "+sequance[0]+"="+str(sequance[1])+";"
        print(sql)
        self.cursor.execute(sql)
        self.connect.commit()
#----------------------------------------------------------------------------------------#
    def updateData(self,table,pw,sequance):
        value=pw
        sql="UPDATE "
        sql+=table+" SET "+""
        sql+=str(value[0])+"="+str(value[1])
        sql+=" WHERE "+sequance[0]+"="+str(sequance[1])
        sql+=";"
        print(sql)
        self.cursor.execute(sql)
        self.connect.commit()
#----------------------------------------------------------------------------------------#
    def readData(self,table,colums,values):  
        userData=[colums,values]
        sql="SELECT *FROM "+table+ " WHERE "
        for index in range(0,len(userData[0])):
            if index!=0:
                sql+=" AND "
            sql+=str(userData[0][index])+"="+"'"+str(userData[1][index])+"'"
        sql+=";"
        print(sql)
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        print(result)
        return result
#----------------------------------------------------------------------------------------#