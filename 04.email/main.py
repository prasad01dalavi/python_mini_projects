import smtplib

from_address = ''
to_address = ''
message = "simple email message, sent using python program"
password = ''

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_address, password)
server.sendmail(from_address, to_address, message)
server.quit()
print 'Email Sent!'
