from myapp.xhqb.db_server import db_server
"""查询maincifdb.t_customer_info表的数据"""
def info_check_phone(identity_no):
    db = db_server()
    cursor = db.cursor()
    info_base={}
    sql="SELECT id,customer_name,identity_no,mobile_phone FROM maincifdb.t_customer_info WHERE identity_no= '%s';"  %(identity_no)
    # print(sql)
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        list_name = ["id", "name", "identity_no", "mobile_phone"]
        info_base = dict(zip(list_name,list(data[0])))
        info_base["success"]=True
        # print(info_base)
    except:
        info_base["success"] = False
        # print(info_base)
        print("查询maincifdb.t_customer_info失败")
    finally:
        cursor.close()
    return info_base

"""修改maincifdb.t_customer_info表的数据"""
def update_info(id,up_identity_no=None,up_name=None,up_phone=None):
    db = db_server()
    cursor = db.cursor()
    sql="UPDATE maincifdb.t_customer_info SET identity_no='%s',customer_name='%s',mobile_phone='%s' where id='%s' ;" % (up_identity_no,up_name,up_phone,id)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("maincifdb.t_customer_info数据修改成功")
    except:
        db.rollback()
        print("maincifdb.t_customer_info数据修改失败")
    finally:
        cursor.close()

if __name__=="__main__":
    info_check_phone("3412031963052634151")