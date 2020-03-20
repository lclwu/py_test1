from db_server import db_server

""""通过手机号查询客户信息，返回：cid、name、identity_no、mobile_phone"""
def base_check_phone(phone):
    db = db_server()
    cursor = db.cursor()
    cif_base={}
    sql="SELECT id,customer_name,identity_no,mobile_phone FROM cifdb.t_customer_base WHERE mobile_phone= '%s';"  %(phone)
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        data1=list(data[0])
        list_name=["cid","name","identity_no","mobile_phone"]
        cif_base=dict(zip(list_name,data1))
        cif_base["success"]=True
        # print(cif_base)

    except:
        cif_base["success"] = False
        print("查询cif_base失败")
    finally:
        cursor.close()
    return cif_base
""" 身份证号查询客户信息，返回：cid、name、identity_no、mobile_phone"""
def base_check_identity(identity_no):
    db = db_server()
    cursor = db.cursor()
    cif_base = {}
    sql="SELECT id,customer_name,identity_no,mobile_phone FROM cifdb.t_customer_base WHERE identity_no= '%s';"  %(identity_no)
    # print(sql)
    try:
        cursor.execute(sql)
        data = cursor.fetchmany(1)
        data1=list(data[0])
        list_name=["cid","name","identity_no","mobile_phone"]
        cif_base=dict(zip(list_name,data1))
        # print(cif_base)
        cif_base["success"] = True

    except:
        cif_base["success"] = False
        print("查询cif_base失败")
    finally:
        cursor.close()
    return cif_base
"""判断用户传的是身份证号还是手机号"""
def base_check(phone=None,identity_no=None):
    if phone!=None:
        data_base=base_check_phone(phone)
    elif identity_no !=None:
        data_base=base_check_identity(identity_no)
    else:
        print("请输入手机号或者身份证号")
    return data_base




"""修改cifdb.t_customer_base表的数据"""
def update_base(cid,up_identity_no,up_name,up_phone):
    db = db_server()
    cursor = db.cursor()
    sql="UPDATE cifdb.t_customer_base SET identity_no='%s',customer_name='%s',mobile_phone='%s' where id='%s';" % (up_identity_no,up_name,up_phone,cid)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("cifdb.t_customer_base数据修改成功")
    except:
        db.rollback()
        print("cifdb.t_customer_base数据修改失败")
    finally:
        cursor.close()

if __name__=="__main__":
    base_check_phone("18973599071")
