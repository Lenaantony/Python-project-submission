import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "lenaantony7102006@gmail.com"
receiver_email = "lenaantony7617@gmail.com"

password = "tnid gexr kuiw zxfv"


subject = "Test News Email"
body = "<h1>html #from news scraper</h1>"


msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "html"))


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, password)
server.send_message(msg)
server.quit()

print("Email sent")