# creating a tuple taking user_input with multiple data type,printing the element of user choice, unpacking the elements
user_length = int(input("Enter the length of the tuple: \n"))
"""
user_list =[]
while len(user_tuple) < user_length:
    user_element = input("enter the elements of the tuple")
    if user_element.isalnum() or bool or float:
        user_list.append(user_element) 
    else:
        print("enter valid input")
user_tuple = tuple(user_list)
print("user entered tuple is: ", user_tuple)
"""
"""
for i in range(user_length):
    user_element = input("enter the elements of the tuple: \n")
    if user_element.isalnum() or bool or float:
        user_tuple = tuple(user_element)  # taking only one element at a time
    else:
        print("enter valid input")

print("user entered tuple is :", user_tuple)  # local variable cannot be accessed outside loop
"""

user_element = [input("enter the elements of tuple: ") for i in range(user_length)]
user_tuple = tuple(user_element)
print(user_tuple)
user_choice = int(input("Enter the index of the element to be printed"))
print(user_tuple[user_choice])

variable_1, variable_2, *remaining_variables = user_tuple
print(variable_1)
print(variable_2)
print(remaining_variables)
tuple_reverse = user_tuple[::-1]
print(tuple_reverse)

user_string = ''.join(user_tuple)  # converts tuple into string
print(user_string)
print(type(user_string))
