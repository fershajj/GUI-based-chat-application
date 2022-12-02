import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import otpgen

def pwreset(tomail):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)

    server.ehlo()



    server.login('********@gmail.com','**********')

    msg=MIMEMultipart()
    msg['From']='***'
    msg['to']=tomail+'@gmail.com'
    msg['subject']='Reset Password'
    global otp
    otp=otpgen.main()
    message=f"Hello!\nYour OTP for password reset is {otp}"
    msg.attach(MIMEText(message,'plain'))

    text=msg.as_string()
    server.sendmail('******@gmail.com',tomail+'@gmail.com',text)

def main(tomail):
    pwreset(tomail)
    return otp

    