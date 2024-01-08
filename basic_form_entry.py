import re

# creating user id using if statement
"""
user_id = input("enter valid user id : \n")
common_id = ['abc12', 'xyz12']
#if user_id.isalnum():
#print("user id created")
if len(user_id) == 5 and user_id not in common_id and user_id.isalnum():
    print("User id entered successfully")
elif user_id == (''):
    print("Do not enter blank or spaces in user id")
elif user_id.isspace():
    print("spaces are not allowed")
else:
    print("enter valid user_id")
"""
# creating user id and password using regular expressions
common_user_ids = ["abc12", "def23", "xyz34"]
common_passwords = ["pass@123", "qwer!234", "secure123"]

while True:
    user_id = input("Enter your user id ( 3 letters and 2 numbers) : \n")
    if re.match("^[a-zA-Z]{3}\d{2}$", user_id) and user_id not in common_user_ids:
        print("Valid user id entered")
        break
    else:
        print("Enter valid user id")
    continue

while True:
    password = input("Enter your password ( 4 Letters ,1 special character and 3 numbers) : \n")
    if re.match("^[a-zA-Z]{4}[!@#$%^&*()-_=+]{1}\d{3}$", password) and password not in common_passwords:
        print("Valid password entered")
        break
    else:
        print("Enter Valid password")
        continue
