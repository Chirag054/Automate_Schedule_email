import smtplib, ssl
import requests
import time

def sendMail():
    smtp_server = "smtp.gmail.com"                # gmail server
    port = 587                                    # For starttls
    sender_email = "sender-mail-id"               #sender's mail id
    receiver_email  = ['reciever-mail-id']        #list of reciever's mail ids
    password = "enter-your-password-here"

    


    subject="Daily Mail"
    
    text = 'Good morning!'
    message = 'Subject: {}\n\n{}'.format(subject, text)
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()                               # Can be omitted
        server.starttls(context=context)            # Secure the connection
        server.ehlo()                               
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    
    except Exception as e:
        print(e)


