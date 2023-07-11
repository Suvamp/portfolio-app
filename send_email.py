import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user_email = "suvamp@uci.edu"
password = "dltoscijeurxzehw"

receiver = "patelsuvam621@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hello!
Hello.

I am away at the moment. Someone from our team should reach out to you ASAP. 


Best Regards,


Suvam Patel
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_email, password)
    server.sendmail(user_email, receiver, message)

