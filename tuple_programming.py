# user_length = int(input("Enter the length of the tuple"))
# for i in range(user_input):
#     user_element = input("Enter the tuple element")
#     user_tuple = tuple(user_element)
#     print(user_tuple)

# user_element = [input("Enter the tuple elements: ") for i in range(user_length)]
# user_tuple = tuple(user_element)
# print(user_tuple)
#
# if len(user_tuple) >= 4:
#     print(user_tuple[-4])
# else:
#     print("Length of tuple is less than 4")

# repeated items in a tuple
# user_length = int(input("Enter the length of the tuple: \n"))
# user_element = [input("Enter the tuple elements: \n") for i in range(user_length)]
# user_tuple = tuple(user_element)
# print(user_tuple)
#
# for i in user_tuple:
#     if user_tuple.count(i) > 1:
#         print(i)

# check whether an element exists within a tuple
# user_length = int(input("Enter the length of the tuple: \n"))
# user_element = [input("Enter the tuple elements: \n") for i in range(user_length)]
# user_tuple = tuple(user_element)
# print(user_tuple)
#
# user_input = input("Enter the element to be searched: \n")
# if user_input in user_tuple:
#     print("Yes the element is available in the tuple")
# else:
#     print("No the element is not available in the tuple")

#  convert list to tuple
# user_length = int(input("Enter the length of the tuple: \n"))
# user_element = [input("Enter the tuple elements: \n") for i in range(user_length)]
# user_list = list(user_element)
# print(user_list)
# print(type(user_list))
# user_tuple = tuple(user_list)
# print(user_tuple)
# print(type(user_tuple))

#  Remove item from tuple
# user_length = int(input("Enter the length of the tuple: \n"))
# user_element = [input("Enter the tuple elements: \n") for i in range(user_length)]
# user_tuple = tuple(user_element)
# print(user_tuple)
# user_list = list(user_tuple)
#
# #  user_item = input("Enter the element to be removed: \n ") # takes string as input
# #  user_item = int(input("Enter the element to be removed: \n")) # invalid literal for int if string is an input
#
# user_input = input("Enter the element to be removed: \n")
# if user_input in user_list:
#     # user_list.pop(user_input) -->string cannot be passed into int
#     user_list.remove(user_input)
# else:
#     print("Item not found")
#
# user_tuple = tuple(user_list)
# print(user_tuple)

#  convert a tuple to a dictionary
# user_length = int(input("Enter the length of the tuple: \n"))
# user_element = [input("Enter the tuple elements: \n") for i in range(user_length)]
# user_tuple = tuple(user_element)
# print(user_tuple)
#
# user_input = input("Enter the element whose index is to be found: \n") # find tuple element by index
# if user_input in user_tuple:
#     print(user_tuple.index(user_input))
# else:
#     print("Element not available in tuple")
#
# user_dict = dict(zip(user_tuple[::2], user_tuple[1::2]))  #[::2] takes every 2nd element from 1st as key, [1::2] takes every 2nd element from 2nd as value.
# print(user_dict)
# user_dict_1 = dict(zip(user_tuple, user_tuple))  # each element in tuple acts as a key value pair
# print(user_dict_1)
#  user_key = input("Enter the key for the dictionary: \n")
#  user_dict = dict{user_key: user_tuple} --> syntax error

#  unzip a list of tuples into individual lists
# user_length = int(input("Enter the length of the list: \n"))
# user_list = []
# while len(user_list) < user_length:
#     user_element = eval(input("Enter the user tuple in user list separated by comma: \n"))  #eval is used to make sure user inputs into tuple correctly
#     user_list.append(user_element)
#print(user_list)
#
# individual_list = list(zip(*user_list)) # *zip function is used to unzip it into multiple lists,here first elements of each tuple makes one list, next elements of each tuple makes next list
#
# print(individual_list) # prints a single list with 2 bracket of values
#
# for i, lst in enumerate(individual_list, 1):
#     print("List {}:{}".format(i, lst))

# reverse a tuple
user_length = int(input("Enter the length of the list: \n"))
user_input = [input("Enter the tuple elements: \n") for i in range(user_length)]
user_tuple = tuple(user_input)
print(user_tuple)

user_tuple_1 = user_tuple[::-1]

print(user_tuple_1)