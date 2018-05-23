import smtplib

from_address = 'prasad01dalavi@gmail.com'
to_address = ''

message = "simple email message, sent using python program"

passwd = raw_input("Please enter your password:")

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_address, passwd)
server.sendmail(from_address, to_address, message)
server.quit()
print 'Email Sent!'
