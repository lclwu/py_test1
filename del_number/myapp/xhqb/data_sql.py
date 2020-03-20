# import pymysql
# from db_server import db_server
#
# """通过手机号查询客户信息，返回：cid、name、identity_no、mobile_phone"""
# def cif_base_check_phone(phone):
#     cursor=db_server()
#     sql="SELECT id,customer_name,identity_no,mobile_phone FROM cifdb.t_customer_base WHERE mobile_phone= '%s';"  %(phone)
#     try:
#         cursor.execute(sql)
#         data = cursor.fetchmany(1)
#         data1=list(data[0])
#         list_name=["cid","name","identity_no","mobile_phone"]
#         cif_base=dict(zip(list_name,data1))
#         # print(cif_base)
#         return cif_base
#     except:
#         print("查询cif_base失败")
#     finally:
#         cursor.close()
#
# """ 身份证号查询客户信息，返回：cid、name、identity_no、mobile_phone"""
# def cif_base_check_identity(identity_no):
#     cursor=db_server()
#     sql="SELECT id,customer_name,identity_no,mobile_phone FROM cifdb.t_customer_base WHERE identity_no= '%s';"  %(identity_no)
#     try:
#         cursor.execute(sql)
#         data = cursor.fetchmany(1)
#         data1=list(data[0])
#         list_name=["cid","name","identity_no","mobile_phone"]
#         cif_base=dict(zip(list_name,data1))
#         # print(cif_base)
#         return cif_base
#     except:
#         print("查询cif_base失败")
#     finally:
#         cursor.close()
#
# """遍历数据库表是否有数据，有数据的通过返回一个list"""
# def muber_check(cid,identity_no):
#     cursor = db_server()
#     tabel_list=["oidc.user_partner_bind","cifdb.t_customer_credentials",'cifdb.t_customer_md5','cifdb.t_customer_partner ']
#     for i in tabel_list:
#         sql1 = "SELECT id FROM %s WHERE cid= '%s';" % (i, cid)
#         sql2 = "SELECT id FROM maincifdb.t_customer_info WHERE identity_no= '%s';" % (identity_no)
#         # print(sql1)
#         try:
#             cursor.execute(sql1)
#             data = cursor.fetchmany(1)
#             # print(data)
#         except:
#             print("=========="+i+'没有数据')
#             tabel_list.remove(i)
#     try:
#         cursor.execute(sql2)
#         data = cursor.fetchmany(1)
#         # print(data)
#         tabel_list.append(i)
#     except:
#         print('=========='+i+'没有数据')
#         tabel_list.remove(i)
#
#     cursor.close()
#     print(tabel_list)
#
#
# def muber_update(addlist=[]):
#     cursor = db_server()
#     up_sql=
#     try:
#         for i in addlist:
#             pylist=["cifdb.t_customer_base","maincifdb.t_customer_info"]
#             if (i in pylist)==False:
#
#
#
#
#
#
# if __name__=="__main__":
#     big= cif_base_check_phone("18973599071")
#     # cif_base_check_identity("431027199309302616")
#     muber_check(big["cid"], big["identity_no"])
