import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

from testreport.configemail import ConfigEmail


def send_email(test_time):
    email = ConfigEmail("./email_address.ini")
    mail_host = email.get_smtp()  # 设置服务器
    mail_user = email.get_login()  # 用户名
    mail_pass = email.get_authorization_code()  # 口令

    sender = email.get_sender()
    receivers = email.get_to().split(",")
    # 创建一个带附件的实例
    message = MIMEMultipart()
    # message = MIMEText("data", 'plain', 'utf-8')
    message['From'] = Header("接口测试报告"+test_time, 'utf-8')
    message['From'] = email.get_sender()
    message['To'] = receivers[0]
    subject = '接口自动化测试报告'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    att1 = MIMEApplication(open("./Report/"+test_time+".html", 'rb').read())
    att1.add_header('Content-Disposition', 'attachment', filename=test_time+'.html')
    # att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = '接口测试报告'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP(timeout=25)
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


if __name__ == "__main__":
    send_email(test_time="123")
