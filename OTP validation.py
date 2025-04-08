import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body = f"OTP for Verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "snmaheshvanagudi@gmail.com"
msg["To"] = input("Enter Email Id: ")
msg["Subject"] = "OTP For Validation"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("snmaheshvanagudi@gmail.com","opll furz edxp lqld")
server.send_message(msg)
server.quit()

cotp = int(input("Enter OTP Recieved: "))
if otp == cotp:
    print("OTP Verification Success")
else:
    print("Invalid OTP")







