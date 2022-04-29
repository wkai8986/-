#!/usr/bin/python3 
import pymysql  


class DB():
    def __init__(self, host='192.168.224.128', port=3306, db='interfaces', user='root', passwd='123456', charset='utf8'):
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
        

    def insert(self, i_name, i_addr):
        sql = "INSERT INTO `ixp_interfaces` (`i_name`, `i_addr`) VALUES ('" + i_name + "','" + i_addr + "')"
        self.cur.execute(sql)
        self.conn.commit()

    def query(self):
        sql = "SELECT * FROM `ixp_interfaces`"
        self.cur.execute(sql)
        return self.cur.fetchall()
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
