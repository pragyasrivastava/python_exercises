# take upto 3-digit user input using length function
"""
user_input = input("Enter the number: ")
if len(user_input) <= 3 and user_input.isdigit():
    print('The user entered ' + user_input + ' valid entry')
else:
    print(' The user entered ' + user_input + ' is invalid entry')
"""
#  take only positive input from user
"""
user_input = int(input("Enter the number: "))
if user_input <= -1:
    print( 'Invalid Input')
else:
    # print (f'You entered: {user_input} is valid') - f string supported for python 3.6 and above
    print('Valid Input')
"""
#  Take user input using try except block and not take blank or white space entry
while True:
    num = input("Enter an integer 0-999: \n").strip()
    if not num:
        print("Please enter non-empty value")
    try:
        num = int(num)
    except ValueError:
        print("Please enter a valid integer 0-999")
        continue
    if num >= 0 and num <= 999:
        print("The integer is in the range 0-999")
        break
    else:
        print("The integer must be in the range 0-999")