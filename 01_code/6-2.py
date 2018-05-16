#가상의 이메일 전송 함수

def send_mail(from_mail,to_mail,subject,contents):
    print("From: \t"+from_mail)
    print("To: \t"+to_mail)
    print("subject:"+subject)
    print("*"*20)
    print(contents)
    print("*"*20)
    print("*"*20)

my_email = "ysjk2003@hanmail.net"

users = []
users.append({'name':'Boo','email':'ysjk2003@naver.com'})
users.append({'name':'john','email':'ysjk2003@gmail.com'})

contents = "hello mr.kim"

for user in users:
    title = 'Dear. '+user['name']
    send_mail(my_email,user['email'],title,contents)