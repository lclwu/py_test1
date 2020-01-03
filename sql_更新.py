import pymysql

db=pymysql.connect(user='root',password='lcl123456',database='test')

cursor=db.cursor()

sql="UPDATE test_user SET user_name='小旺' WHERE user_name='小红'"
try:
    cursor.execute(sql)
    db.commit()
except:
    #执行失败回滚
    db.rollback()
    print("执行失败")
