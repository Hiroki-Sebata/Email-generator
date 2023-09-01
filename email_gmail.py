import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) #this code make the HTML into text

#========================== this is the receiver email address information ======================
email = EmailMessage()    
email['from'] = 'Hiroki'
email['to'] = 'sebasuta@gmail.com'
email['subject'] = 'the message goes here'

#email.set_content(html.substitute(name = 'abc'),'html') #this is the template class method with "substitute" the name in this code is from "index.html with $name" if you put $, it can be replaced by using template

#=========================== this is the sender's email address information with using the email server such as gmail =======================

with smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465) as smtp: #had to use SMTP_SSL to encrypt the server
    smtp.ehlo()
    #smtp.starttls()#encryption mechanism to secure the server
    smtp.login('youremail@gmail.com', '*********') #not the gmail login password but the app password generated in google account
    smtp.send_message(email)
    
   