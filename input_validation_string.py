# Taking any single character as input
"""
while True:
    user_input = input("Enter a single character: \n")
    if len(user_input)==1:
        print(user_input)
        break
    else:
        print("Enter single character to continue")
        continue
"""
# Taking only single letters as input
"""
while True:
    user_input = input("Enter a single letter: \n")
    if len(user_input) == 1 and user_input.isalpha():
        print("Letter you have entered is " + user_input)
        break
    else:
        print("Enter single letter to continue")
        continue
"""

# Taking only yes or no as input
user_input = input('Do you want to continue (yes/no): \n')
yes_acceptable = ['yes',  'y']
no_acceptable = ['no', 'n']
if user_input.lower() in yes_acceptable:
    print('User wishes to continue')
elif user_input.lower() in no_acceptable:
    print('User does not wish to continue')
else:
    print ('Enter either yes or no to continue')

