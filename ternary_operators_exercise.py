meaning = 2
'''meaning *= 10
print(meaning)
meaning /= 10
print(meaning)
round(meaning)
print(meaning) #here meaning variable is printed which is not yet assigned to round function
meaning = round(meaning)
print(meaning)'''
'''print('')  # Blank space
if meaning > 10:
    print("Right on !")
else:
    print("Not Today")'''

# ternary operator use
print('Right On !') if meaning > 10 else print('Not Today')

name = 'Pragya'
name1 = 'Srivastava'
fullname = name + ' ' + name1  # quote is added for space
print(fullname)
