import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_email = "suvamp@uci.edu"
    password = "dltoscijeurxzehw"

    receiver = "patelsuvam621@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)



