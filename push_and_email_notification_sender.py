import requests, time, smtplib
from notify_run import Notify
from datetime import datetime


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('thadaninilesh19@gmail.com', 'irnhqaqzvunliayt')
    subject = "Python push notification email"
    body = "Testing the body of python scripting push notification and email"
    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(
        'thadaninilesh19@gmail.com',
        'thadaninilesh@hotmail.com',
        msg
        )
    print("Hey! Email has been sent")
    server.close()

def push_notification():
    notify = Notify()
    notify.send("Let Nilesh know that you have received this message")
    print("Notification has been pushed")

count = 0
while(True):
    count += 1
    print("Count: "+str(count))
    send_mail();
    push_notification()
    time.sleep(1000)
