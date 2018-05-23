import way2sms

username = raw_input("Enter your username:")
password = raw_input("Enter your password:")
# Enter the creadentials (by default string formatted due to raw_input)

message = way2sms.sms(username, password)
# create a message instance

recipient_number = ''  # mobile number of the receiver
text_message = "Hey this is my text message!"

message.send(recipient_number, text_message)
print("Message Sent!")

sent_count = message.msgSentToday()
print("Message Sent count:", sent_count)

message.logout()  # logout
print('Successfully Logged out!')
