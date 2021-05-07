# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

SMTP_USER = 'ysjk2003@gmail.com'
SMTP_PASSWORD = ''

def send_mail(name,addr):
    msg = MIMEMultipart()

    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name+'님에게 메일이 도착하였습니다'

    contents = name + '''님에게 메일이 도착하였습니다.
    안녕하세요 자동화로 니컴퓨터 해킹할거야'''

    #msg['text'] = contents

    text = MIMEText(_text = contents, _charset = 'utf-8')
    msg.attach(text)

    #SMTP로 접속할 서버 정보를 가진 클래스 변수를 생성한다.
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    smtp.login(SMTP_USER, SMTP_PASSWORD)

    smtp.sendemail(SMTP_USER, addr, msg.as_string())

    print("\n 이메일이 전송되었습니다 \n")

    smtp.close()

send_mail('김민규','ysjk2003@naver.com')
