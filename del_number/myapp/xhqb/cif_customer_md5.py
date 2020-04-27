from myapp.xhqb.db_server import db_server

def update_md5(up_identity_no, up_phone):
    db = db_server()
    cursor = db.cursor()
    sql="UPDATE cifdb.t_customer_md5 SET mobile_phone='f10a',identity_no='f10a' where identity_no=MD5('%s') or mobile_phone=MD5('%s');" % (up_identity_no, up_phone)

    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("t_customer_md5数据修改成功")
    except:
        db.rollback()
        print("t_customer_md5数据不存在")
    finally:
        cursor.close()