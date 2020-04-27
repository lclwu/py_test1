from myapp.xhqb import cif_customer_base
from myapp.xhqb import maincifdb_customer_info
from myapp.xhqb import  cifdb_customer_credentials
from myapp.xhqb import cif_customer_md5
from myapp.xhqb import cif_customer_partner
from myapp.xhqb import up_identity

from myapp.xhqb.locahost_mober import locahost_mober,inst_names

def base_check_update(phone=None, identity_no=None):
    """修改cif_customer_base表数据"""
    data_base=cif_customer_base.base_check(phone,identity_no)

    grep_id = {"success": True}
    while grep_id["success"] == True:
        up_identity_no = (up_identity.generate_random_str(2) + data_base["identity_no"])
        grep_id = cif_customer_base.base_check(identity_no=up_identity_no)
        print(up_identity_no)

    moble_id = {"success": True}
    while moble_id["success"] == True:
        up_phone = (up_identity.generate_random_str(2) + data_base["mobile_phone"])
        moble_id = cif_customer_base.base_check(up_phone)
        print(up_phone)

    # print(data_base)
    # print(up_date)
    if data_base["success"]==True:
        """修改cifdb.t_customer_base数据"""
        cif_customer_base.update_base(data_base["cid"],up_identity_no,data_base["name"],up_phone)
    #     update_base(cid, up_identity_no, up_name, up_phone)


        """修改maincifdb.t_customer_info数据"""
        info_base=maincifdb_customer_info.info_check_phone(data_base["identity_no"])
        if info_base["success"]==True:
            maincifdb_customer_info.update_info(id=info_base["id"], up_identity_no=up_identity_no, up_name=data_base["name"], up_phone=up_phone)

        """修改cifdb.t_customer_credentials数据"""
        credentials_base=cifdb_customer_credentials.credentials_check(data_base["identity_no"])
        # print(credentials_base)
        if credentials_base["success"] == True:
            cifdb_customer_credentials.credentials_update(credentials_base["id"],up_identity_no=up_identity_no)

        """修改cifdb.t_customer_md5数据"""
        cif_customer_md5.update_md5(up_identity_no,up_phone=up_phone)

        """修改cifdb.t_customer_partner数据"""
        cif_customer_partner.partner_check(data_base["cid"])

        # inst_names(up_identity_no=up_date["up_identity_no"], up_phone=up_phone)
        return "修改成功"
    else:
        return "修改失败!"




if __name__=="__main__":
    # base_check_update(identity_no=1234567890123507)
    a=base_check_update(18670335754)
    print(a)