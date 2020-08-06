import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

to_add = " "
from_add = " "
msg = MIMEMultipart()
msg['From'] = to_add
msg['To'] = from_add
msg['Subject'] = 'Test mail'

body = 'Type body of mail here'

email = ''
password = ''

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(from_add,to_add,text)
mail.quit()