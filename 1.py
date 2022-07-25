# -*- coding:utf-8 -*-
'''
作者：曼曼黑科技
说明：
安装在自己电脑上，可以不用开机密码，别人动你电脑时，
会触发程序启动进行截图，可以自己百度 “开机启动程序如何设置”
自己设置开机自启就行了，可以自行改动设置通知方式等发送给你自己
（获取IP和定位后续再搞）

程序：(由于某些原因，没有生成exe打包文件，自己百度pyinstaller库用法自行生成exe文件)
成品自己下载，也可以自己下载源码修改，未经允许不得用于商业用途。
'''



import re
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


cap = cv2.VideoCapture(0)

while(1):
    # 获得图片
    ret, frame = cap.read()
    cv2.imwrite("camera.jpg", frame)
    break
cap.release()
cv2.destroyAllWindows()


# 使用readline()读文件，获取zh_pwd.ini文件的账号和授权码
f = open("zh_pwd.ini",mode='r',encoding='utf-8')
line=f.readlines()
zh=re.search("(?<=')\w+",line[1]).group(0)
pwd=re.search("(?<=')\w+",line[2]).group(0)
f.close()


msg_from = zh+'@qq.com'  # 发送方邮箱

passwd = pwd  # 填入发送方邮箱的授权码(不会就百度qq邮箱授权码)
msg_to = zh+'@qq.com'  # 收件人邮箱，我是自己发给自己
text_content = "\n主人，有人动你电脑！！！\n\n主人，有人动你电脑！！！\n\n主人，有人动你电脑！！！" # 发送的邮件内容
file_path = 'camera.jpg' # 需要发送的附件目录

# 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
def send_email(msg_from, passwd, msg_to, text_content, file_path=None):
    msg = MIMEMultipart()
    subject = "紧急通知："  # 主题
    text = MIMEText(text_content)
    msg.attach(text)


    if file_path:  # 最开始的函数参数默认设置了None ，想添加附件，自行更改一下就好
        docFile = file_path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
        msg.attach(docApart)
        print('发送附件！')
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()


send_email(msg_from,passwd,msg_to,text_content,file_path)



