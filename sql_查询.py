import pymysql

# 链接数据库
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="lcl123456",database="test")
cursor=db.cursor()
sql="SELECT * FROM test.test_user WHERE user_name='小红'"
cursor.execute(sql)
#返回一行的数据
# print(cursor.fetchone())

# 返回size行的数据
print(cursor.fetchmany(2))

# 返回所以行的数据
# data=cursor.fetchall()
# for i in data:
#     print(i)
