#!/usr/bin/python3 
import pymysql  
from configparser import ConfigParser

class DB():

    # 读取数据库连接信息
    conf = ConfigParser()
    conf.read("interfaceTest.config","utf-8")
    host = conf.get("mysql","host")
    port = conf.getint("mysql","port")
    db = conf.get("mysql","db")
    user = conf.get("mysql","user")
    passwd = conf.get("mysql","passwd")


    def __init__(self, host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标        
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()
        

    def addInterface(self, i_name, i_addr):
        sql = "INSERT INTO `ixp_interfaces` (`i_name`, `i_addr`) VALUES ('" + i_name + "','" + i_addr + "')"
        self.cur.execute(sql)
        self.conn.commit()

    def findAllInterfaces(self):
        sql = "SELECT * FROM `ixp_interfaces`"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def findFunctions(self):
        pass
    def addFunction(self):
        pass

    def close(self):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()
    
    
   
'''  
db = pymysql.connect(host='192.168.224.128', port=3306, user='root', password='123456', db='interfaces')
cursor = db.cursor()

def insert(i_name, i_addr):
    print("***********")
    sql = "INSERT INTO `ixp_interfaces` (`i_name`, `i_addr`) VALUES ('" + i_name + "','" + i_addr + "')"
    cursor.execute(sql)
    close()
 
 
def close():
    db.commit()
    cursor.close()
    db.close()
'''   
