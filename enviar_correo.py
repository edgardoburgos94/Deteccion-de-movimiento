import smtplib

content = 'Example email stuff here'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('edgardo.burgos94@gmail.com','e1d9b9a4')

mail.sendmail('edgardo.burgos94@gmail.com','edgardo.burgos94@gmail.com',content)

mail.close()
