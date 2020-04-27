from myapp.xhqb.db_server import db_server

def partner_check(cid):
    db = db_server()
    cursor = db.cursor()
    cif_base={}
    sql="select id,partner_id from cifdb.t_customer_partner where cid='%s';"  %(cid)
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        data1=list(data[0])

        try:
            sql="UPDATE cifdb.t_customer_partner SET partner_id=1 where id='%s'"%(data1[0])
            cursor.execute(sql)
            db.commit()
            print("更新cifdb.t_customer_partner成功")
        except:
            print("更新cifdb.t_customer_partner失败")


    except:
        cif_base["success"] = False
        cif_base["mags"]="查询cifdb.t_customer_partner失败"
        print("查询cifdb.t_customer_partner失败")
    finally:
        cursor.close()
    return cif_base

if __name__=="__main__":
    partner_check("20200417000004015020")