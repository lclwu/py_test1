from myapp.xhqb2.db_server import db_server
import json

def send_msg(number):
    # sql = "SELECT id,idcard_no FROM cifdb.t_customer_credentials WHERE idcard_no= '%s';" % (identity_no)
    sql="SELECT send_to_num,send_para,send_time from sms.t_msg_send_log where send_to_num='%s'  and use_template_id='verify-h5Loan-24257'  ORDER BY send_time DESC LIMIT 3;" %(number)
    db = db_server()
    cursor = db.cursor()
    credentials_base={}
    list1=[]
    try:
        cursor.execute(sql)
        data = list(cursor.fetchmany(1)[0])
        print(data[1][0:5])
        a=str(data[2])
        credentials_base={"number":data[0], "send_para":(data[1][0:5]),"time":str(data[2])}
        print(credentials_base)
    except:
        credentials_base["success"] = False
        credentials_base["mags"] = "查询短信验证码失败"
        print("查询短信验证码失败")
    finally:
        cursor.close()
    return credentials_base


if __name__=="__main__":
    send_msg(18973599071)