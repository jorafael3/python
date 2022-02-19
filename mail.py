import smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
smtp_server = "mail.cartimex.com"
gmail_user = 'jalvarado'
gmail_password = 'viernes.2805'

sender_email = "jalvarado@cartimex.com"
receiver_email = "jalvaradoe3@gmail.com"


message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
  <h1 style="color:red">HOLLLLLa</h1>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

filename = "ejerr.py"  # In same directory as script

with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
message.attach(part)

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.ehlo()
        #server.starttls() # Secure the connection
        server.login(gmail_user, gmail_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()

        print ('Email sent!')
except Exception as e:
    print (e)