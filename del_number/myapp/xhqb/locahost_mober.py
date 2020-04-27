from myapp.xhqb.db_server import db2_server
def locahost_mober():
    db2=db2_server()
    cursor = db2.cursor()
    # sql="SELECT * FROM test.ppd_name WHERE customer_name='小红' "
    sql = "SELECT * FROM test.ppd_name ORDER BY create_date DESC"
    cursor.execute(sql)
    i = cursor.fetchone()

    name = i[0]
    identity_no = int(i[1]) + 1
    phone = int(i[2]) + 1
    cursor.close()
    return {"up_name":name,"up_identity_no":identity_no,"up_phone":phone}


def inst_names(up_identity_no,up_phone):
    db = db2_server()
    cursor = db.cursor()
    sql1 = "INSERT INTO test.ppd_name (customer_name,identity_no,mobile_phone,create_date) VALUES ('小黄',%s,%s,sysdate())" % (str(up_identity_no), str(up_phone))
    print(sql1)
    cursor.execute(sql1)
    db.commit()
    print("插入数据成功")
    cursor.close()

if __name__=="__main__":
    a=locahost_mober()
    print(a)
    inst_names(1234567890123507, 12100000051)
