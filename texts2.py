from py_imessage import imessage

phone = "0123456789" #10 digit number

script = open('script.txt','r')
lines = script.readlines()

for line in lines: 
    if not line.strip():
        continue
    imessage.send(phone, line.strip())