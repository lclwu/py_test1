from myapp.xhqb import cif_customer_base
from myapp.xhqb import maincifdb_customer_info
from myapp.xhqb import  cifdb_customer_credentials
from myapp.xhqb import cif_customer_md5
from myapp.xhqb import cif_customer_partner
from myapp.xhqb import up_identity

from myapp.xhqb.locahost_mober import locahost_mober,inst_names

def base_check_update(phone=None, identity_no=None):
    # """修改cif_customer_base表数据"""
    # grep_id={"success":True}
    # while grep_id["success"] ==True:
    #     data_base=cif_customer_base.base_check(phone,identity_no)
    #     up_date = (up_identity.generate_random_str(2) + data_base["identity_no"])
    #     grep_id = cif_customer_base.base_check(identity_no=up_date)

    moble={"success": True}
    while moble["success"] == True:
        data_base = cif_customer_base.base_check(phone, identity_no)
        print(data_base)
        up_phone = (up_identity.generate_random_str(2) + data_base["mobile_phone"])
        moble=cif_customer_base.base_check(up_phone)
        print(moble)
        print(up_phone)



if __name__=="__main__":
    base_check_update(18973599071)