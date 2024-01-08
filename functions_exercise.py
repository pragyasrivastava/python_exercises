# max of 3 numbers using function
# def max_number(x, y, z):
#     return max(x, y, z)
#
# print(max_number(1, 2, 3))

# max of 3 numbers taking user input:
# def max_number(num1, num2, num3):
#     return max(num1, num2, num3)
#
# try:
#     num1 = int(input("Enter the value 1: \n"))
#     num2 = int(input("Enter the value 2: \n"))
#     num3 = int(input("Enter the value 3: \n"))
#     result = max_number(num1, num2, num3)
#     print("The maximum value is : ", result)
#
# except ValueError:
#     print("Invalid Input")

# factorial of a number using function:
# def factorial_number(num):
#     if num < 0:
#         return "Please enter positive number"
#     elif num == 0 or num == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, num + 1):
#             result = result*i
#         return result
#
# num = int(input("Enter the value"))
# fact_value = factorial_number(num)
# print(fact_value)

# Python function that accepts a string and counts the number of upper and lower case letters
# def string_count(user_string):
#     upper_case_count = 0
#     lower_case_count = 0
#     """
#     incorrect increment
#     for _ in user_string:
#         if user_string.isupper():
#             upper_case_count = upper_case_count + 1
#         else:
#             lower_case_count = lower_case_count + 1
#
#     return upper_case_count, lower_case_count
#     """
#     for c in user_string:
#         if c.isupper():
#             upper_case_count = upper_case_count + 1
#         elif c.islower():
#             lower_case_count = lower_case_count + 1
#         else:
#             pass
#
#     return upper_case_count, lower_case_count
#
# try:
#     user_string = input("Enter the string to be counted: \n")
#     if user_string.isdigit():
#         print("Enter only string value")
#     else:
#         string_value_count = string_count(user_string)
#         print("The upper case and lower case values are:\n", string_value_count)
#
# except ValueError:
#     print("Invalid input")

# to print the even numbers from a given list.
# def even_value_list(input_list):
#     even_list = []
#     #for i in range(input_list): --> 'list' object cannot be interpreted as an integer
#     for i in input_list:
#         #if (i % 2 == 0): --> TypeError: not all arguments converted during string formatting
#             even_list.append(i)
#         else:
#             pass
#     return even_list
#
# user_length = int(input("Enter the length of the list"))
# user_list = []
# for _ in range(user_length):
#     user_element = input("Enter user element")
#     if user_element.isdigit():
#         user_list.append(user_element)
#     else:
#         print("Enter only positive integers")
#
# print(user_list)
# even_value_list(user_list)
# even_value_list(user_list) --> File "/home/pragya/PycharmProjects/pythonlearning/functions_exercise.py", line 92, in <module>even_value_list(user_list)
# print("The even number list is: ", even_value_list(user_list)) -->File "/home/pragya/PycharmProjects/pythonlearning/functions_exercise.py", line 93, in <module>print("The even number list is: ", even_value_list(user_list))
