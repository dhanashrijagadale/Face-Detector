import re
email_condition = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
user_email=input("Enter your Email: ")
if re.search(email_condition,user_email):
    print("Well Done")
else:
    print("Try Again")
