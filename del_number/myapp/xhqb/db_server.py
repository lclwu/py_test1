import pymysql
def db_server():
    host = "xhtestdb01.cq5skzcvpodr.rds.cn-north-1.amazonaws.com.cn"
    port = 3306
    user_name = "lichaolong"
    password = "9569fe195ee6"
    db=pymysql.connect(host=host,port=port,user=user_name,password=password)
    return db


