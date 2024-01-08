# convert list of tuples into dictionary
# user_length = int(input("Enter the length of the list: \n"))
# user_lists = []
# for i in range(user_length):
#     user_element = eval(input("Enter the values of tuple separated by a comma: \n"))
#     user_lists.append(user_element)
# print(user_lists)
# #user_dict = dict(zip(user_list)) # error as dictionary update sequence element #0 has length 1; 2 is required
# user_dict_1 = dict(user_lists)
# print(user_dict_1)
# user_dict = dict(zip(user_lists, user_lists)) # each tuple acts as a key-value pair
# print(user_dict)

# Print a tuple with string formatting
# user_length = int(input("Enter the tuple length: \n"))
# user_input = [input("Enter the input for tuple: \n") for i in range(user_length)]
# user_tuple = tuple(user_input)
# print("This is a tuple", user_tuple)
# print('This is a tuple {}'.format(user_tuple))
# print(type(user_tuple))

# To replace the last value of tuples in a list.
user_length = int(input("Enter the length of the list of tuples: \n"))
user_list = []
# while len(user_list) < user_length:
#     user_element = eval(input("Enter the tuple elements separated by comma: \n"))
#     user_list.append(user_element)

for _ in range(user_length):
    user_input = input("Enter the tuple elements: \n") #-->takes string as input
    #user_input = int(input("Enter the tuple elements")) -- doesn't take multiple values as input
    user_input = eval(user_input)
    user_list.append(user_input)

"""
try:
    for _ in range(user_length):
        user_input = input("Enter the tuple elements: \n") #-->takes string as input
        user_tuple = tuple(map(int, user_input.split()))
        user_list.append(user_tuple)
except ValueError:
    print("Invalid input")
"""
print(user_list)

#user_replace = input("Enter the value to be replaced in each tuple: \n") # this takes input as string
user_replace = int(input("Enter the value to be replaced in each tuple: \n"))
modified_list = []

"""
for i, _ in user_list: # takes only 2 values if tuple has values greater than two it throws error as too many values to unpack (expected 2)
    modified_list.append((i, user_replace))
"""
for i in user_list:
    #modified_list.append((i[:-1], user_replace)) # prints value as [((1, 2), '8'), ((4, 5), '8')]
    modified_list.append((*i[:-1], user_replace))  # * concatenates the elements of i[:-1] with replaced value, element is added as a string if not convert to int type
    #modified_list.append(i[:-1] + (user_replace,)) # it adds the element as a string in the tuple if not converted to int

print("list of tuples before being modified", user_list)
print("List after being modified", modified_list)

# convert list of tuples into dictionary --> covering all loopholes in the above program
