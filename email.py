import smtplib
 
s = smtplib.SMTP('smtp.gmail.com', 587)
s = smtplib.SMTP_SSL(host='localhost', port=80)
s.starttls()
s.login('rehmatnoyda@gmail.com','remat@0105')
message = "hello Rehmat!"
s.sendmail("rehmatnoyda@gmail.com","rehmatnoyda@gmail.com",message)
s.quit()