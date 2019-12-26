# -*- coding:utf-8 -*-
"""发送邮件，text格式"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def my_email(my_text,Subject):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1073343358@qq.com"  # 用户名
    mail_pass = "ezvppdwpwgqhbegi"  # 口令
    receiver = 'lichaolong708@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message=MIMEText(my_text,"plain","utf-8")
    message["From"]=formataddr(["李超龙",mail_user])
    message["To"]=formataddr(["测试小组",receiver])
    message['Subject'] =Subject

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(mail_user,receiver,message.as_string())
        print("发送成功")
    except Exception:
        print("发送失败")


if __name__=="__main__":
    text="时光荏苒，岁月匆匆，年关将至，春节放假三天,\n    我要上学校，花儿对我笑"
    title="放假通知"
    my_email(text,title)