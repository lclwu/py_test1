import pymysql
def db_server():
    host = "xhtestdb01.cq5skzcvpodr.rds.cn-north-1.amazonaws.com.cn"
    port = 3306
    user_name = "lichaolong"
    password = "9569fe195ee6"
    db=pymysql.connect(host=host,port=port,user=user_name,password=password)
    return db


def db2_server():
    db2 = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", database="test")
    return db2
