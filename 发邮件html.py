import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText

def email_html(email_title,email_text):
    email_host="smtp.163.com"
    email_user="lichaolong708@163.com"
    email_password="lcl123456"

    pri_username="1073343358@qq.com"

    imagss=MIMEText(email_text,"html","utf-8")
    imagss["From"]=formataddr(["李超龙",email_user])
    imagss["to"]=formataddr(["测试小组",pri_username])
    imagss["Subject"]=email_title

    try:
        smtpObj=smtplib.SMTP()
        smtpObj.connect(email_host,25)
        smtpObj.login(email_user,email_password)
        smtpObj.sendmail(email_user,pri_username,imagss.as_string())
        print("发送邮件成功")
    except Exception:
        print("发送失败")


if __name__=="__main__":
    a="""
     <p>这是一个美丽的故事</p>
     <a href="https://www.baidu.com" a>小明</a>
    """
    email_html("美丽",a)




