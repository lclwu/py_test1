from db_server import db_server

def credentials_check_identity(tabel,field_list,find,findid):
    db = db_server()
    cursor = db.cursor()
    identity_base = {}
    sd = ','.join(field_list)
    print(sd)
    sql = "SELECT %s FROM %s WHERE %s= '%s';" % (sd,tabel,find,findid)
    print(sql)
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        list_name = field_list
        identity_base = dict(zip(list_name, list(data[0])))
        identity_base["success"] = True
        # print(info_base)
    except:
        identity_base["success"] = False
        # print(info_base)
        print("查询maincifdb.t_customer_info失败")
    finally:
        cursor.close()
    return identity_base

if __name__=="__main__":
    list=["id", "name", "identity_no", "mobile_phone"]
    credentials_check_identity("maincifdb.t_customer_info",list,"identity_no","431027199309302616")