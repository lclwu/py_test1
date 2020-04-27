from myapp.xhqb import cif_customer_base
from myapp.xhqb import maincifdb_customer_info

"""cifdb.t_customer_base表的数据"""
def base_check_update(phone=None, identity_no=None, up_identity_no=None, up_name=None, up_phone=None):
    data_base=cif_customer_base.base_check(phone,identity_no)
    print(data_base)
    if data_base["success"]==True:
        if up_identity_no==None:
            up_identity_no=data_base["identity_no"]
        if up_name==None:
              up_name=data_base['name']
        if up_phone==None:
            up_phone=data_base['mobile_phone']
        cif_customer_base.update_base(data_base["cid"],up_identity_no,up_name,up_phone)

    """判断cif表是否可以查到数据"""
    if identity_no==None and data_base["success"]==True:
        identity_no=data_base["identity_no"]

    """修改maincifdb_customer_info表数据"""
    info_base=maincifdb_customer_info.info_check_phone(identity_no)
    if info_base["success"]==True:
        if up_identity_no==None:
            up_identity_no=info_base["identity_no"]
        if up_name==None:
              up_name=info_base['name']
        if up_phone==None:
            up_phone=info_base['mobile_phone']
        maincifdb_customer_info.update_info(info_base["id"],up_identity_no,up_name,up_phone)


# if __name__=="__main__":


        # maincifdb_customer_info.update_info(data_base["cid"], up_identity_no, up_name, up_phone)







if __name__=="__main__":
    base_check_update(identity_no="51162119610516817X")