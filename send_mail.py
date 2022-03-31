import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ravi.birajdar8880@gmail.com','msfyzwzetkziobeh')
server.sendmail('ravi.birajdar8880@gmail.com','vaijanathgunje62@gmail.com', 'mail sent from python')
print('mail sent')