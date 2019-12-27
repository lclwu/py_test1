# -*- coding:utf-8 -*-
"""发送邮件，text格式"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "lichaolong708@163.com"  # 用户名
mail_pass = "lcl123456"  # 口令

sender = 'lichaolong708@163.com'
receiver='1073343358@qq.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('把钱给我汇过来', 'plain', 'utf-8')
message['From'] = formataddr(["小红",mail_user])
message['To'] = formataddr(["小明",receiver])
subject = '提测邮件'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, [receiver], message.as_string())
    print("邮件发送成功")
except Exception:
    print("发送失败")



# # except smtplib.SMTPException:
# #     print("Error: 无法发送邮件")