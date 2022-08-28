import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("dhanashri.jagadale22@gmail.com","yourpassword")
subject="Pyton"
body="Hello"
message="subject:{}\n\n{}".format(subject,body)
listadd=['dhanashri.jagadale1998@gmail.com',"saurabhjagadale22@gmail.com","dhanashri.jagadale22@gmail.com"]
ob.sendmail("dhanashri.jagadale23@gmail.com",listadd,message)
print("Completed")
ob.quit()