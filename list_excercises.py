# sum of all digits in a given list
"""
numbers = []
while len(numbers) < 5:
    user_input = input("Enter a positive number upto 3-digits: ")
    try:
        number = int(user_input)
        if 0 < number < 1000:
            numbers.append(number)
        else:
            print("Enter positive numbers only")
    except ValueError:
        print("Invalid input, please enter valid number")
result = 0
for num in numbers:
    result +=num

print("sum of numbers is : " + str(result))
"""

# largest and smallest number in a given list
"""
numbers = []
while len(numbers) < 5:
    user_input = input("Enter a positive number")
    try:
        number = int(user_input)
        if 0 < number < 1000:
            numbers.append(number)
        else:
            print("Enter positive numbers only")
    except ValueError:
        print("invalid input")

numbers.sort(reverse=True)
print("Largest number in the list is: " + str(numbers[0]))
numbers.sort()
print("Smallest number in the list is: " + str(numbers[0]))
"""
# sort a list without inbuilt functions
len_of_list = int(input("Enter the length of list : "))
user_list = []
while len(user_list) < len_of_list:
    user_input = int(input("Enter a number upto 3 digit: "))
    try:
        if -1000 < user_input < 1000:
            user_list.append(user_input)
    except ValueError:
        print("Enter valid input for list")

for i in range(len(user_list)):
    for j in range(i+1, len(user_list)):
        if user_list[i] > user_list[j]:
            user_list[i], user_list[j] = user_list[j], user_list[i]

print("Smallest number in list is :" + str(user_list[0]))
print("largest number in list is : " + str(user_list[-1]))