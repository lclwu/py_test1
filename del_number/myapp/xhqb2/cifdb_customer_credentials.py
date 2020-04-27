from myapp.xhqb.db_server import db_server


def credentials_check(identity_no):
    sql = "SELECT id,idcard_no FROM cifdb.t_customer_credentials WHERE idcard_no= '%s';" % (identity_no)
    db = db_server()
    cursor = db.cursor()
    credentials_base={}
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        data1 = list(data[0])
        list_name = ["id", "idcard_no"]
        credentials_base = dict(zip(list_name, data1))
        credentials_base["success"] = True

    except:
        credentials_base["success"] = False
        credentials_base["mags"] = "查询t_customer_credentials失败"
        print("查询t_customer_credentials失败")
    finally:
        cursor.close()
    return credentials_base

def credentials_update(id,up_identity_no):
    db = db_server()
    cursor = db.cursor()
    sql = "UPDATE cifdb.t_customer_credentials SET idcard_no='%s' where id='%s';" % (up_identity_no,id)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("t_customer_credentials数据修改成功")
    except:
        db.rollback()
        print("t_customer_credentials数据修改失败")
    finally:
        cursor.close()


if __name__=="__main__":
    a=credentials_check_identity("431027199309302616k")
    print(a)



# def credentials_check_identity(tabel,field_list,find,findid):
#     db = db_server()
#     cursor = db.cursor()
#     identity_base = {}
#     sd = ','.join(field_list)
#     print(sd)
#     sql = "SELECT %s FROM %s WHERE %s= '%s';" % (sd,tabel,find,findid)
#     print(sql)
#     try:
#         cursor.execute(sql)
#         data = cursor.fetchmany(1)
#         list_name = field_list
#         identity_base = dict(zip(list_name, list(data[0])))
#         identity_base["success"] = True
#         # print(info_base)
#     except:
#         identity_base["success"] = False
#         # print(info_base)
#         print("查询maincifdb.t_customer_info失败")
#     finally:
#         cursor.close()
#     return identity_base
#
# if __name__=="__main__":
#     list=["id", "name", "identity_no", "mobile_phone"]
#     credentials_check_identity("maincifdb.t_customer_info",list,"identity_no","431027199309302616")