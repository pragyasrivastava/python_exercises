# import operator
# combine multiple dicts into one
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for i in (dic1, dic2, dic3):
    dic4.update(i)

print(dic4)
"""
# Sort the dict values into ascending or descending order
# user_length = int(input("Enter the dict length: \n"))
# user_dic = {}
# for _ in range(user_length):
#     user_key = input("Enter the key of the dict: \n")
#     #user_dic.update(user_element)
#     value = input("Enter the value for {}:".format(user_key))
#     user_dic[user_key] = value
#
# print(user_dic)
"""
sorted_asc_dic = dict(sorted(user_dic.items(), key=lambda item: item[1]))

sorted_desc_dic = dict(sorted(user_dic.items(), key=lambda item: item[1], reverse=True))

print("Original dict: ", user_dic)
print("Dict sorted in ascending order: ", sorted_asc_dic)
print("Dict sorted in descending order: ", sorted_desc_dic)
"""
# using operator keyword -->sorting
"""
sorted_asc_dic = dict(sorted(user_dic.items(), key=operator.itemgetter(1)))
sorted_desc_dic = dict(sorted(user_dic.items(), key=operator.itemgetter(1), reverse=True))

print("Original Dict: ", user_dic)
print("Ascending sorted dict: ", sorted_asc_dic)
print("Descending sorted dict: ", sorted_desc_dic)
"""

# sort the dictionary using key
# inherent ordered nature of dict is giving dict in unordered order even after sorting using lambda and operators
"""
sorted_asc_dic = dict(sorted(user_dic.items(), key=operator.itemgetter(0)))
sorted_desc_dic = dict(sorted(user_dic.items(), key=operator.itemgetter(0), reverse=True))

print("Original Dict: ", user_dic)
print("Ascending sorted dict: ", sorted_asc_dic)
print("Descending sorted dict: ", sorted_desc_dic)

sorted_asc_dic = dict(sorted(user_dic.items(), key=lambda item: item[0]))

sorted_desc_dic = dict(sorted(user_dic.items(), key=lambda item: item[0], reverse=True))

print("Original dict: ", user_dic)
print("Dict sorted in ascending order: ", sorted_asc_dic)
print("Dict sorted in descending order: ", sorted_desc_dic)


sorted_dic_asc = dict(sorted(user_dic.items()))
sorted_dic_desc = dict(sorted(user_dic.items(), reverse=True))

print(sorted_dic_asc)
print(sorted_dic_desc)
"""
# add a key to a dictionary
"""
user_length = int(input("Enter the dict length: \n"))
user_dic_1 = {}

for _ in range(user_length):
    user_key = input("Enter the key value: \n")
    user_value = input("Enter the value{} ".format(user_key))
    user_dic_1[user_key] = user_value

print(user_dic_1)

user_input = input("enter the key to be added: \n")
user_input_value = input("enter the value{} ".format(user_input))
#user_dic_1[user_input] = user_input_value  # adds new key and corresponding value to the dict
#user_dic_1.update(user_input, user_input_value) --> atmost 1 argument can be passed in update
#user_dic_1.update({user_input, user_input_value}) #-->error as dictionary update sequence element #0 has length 1; 2 is required
user_dic_1.update({user_input: user_input_value})
print(user_dic_1)
"""
# check whether a given key already exists in a dictionary

"""
user_length = int(input("Enter the dict length: \n"))
user_dic_2 = {}
for _ in range(user_length):
    user_key = input("Enter the key value: \n")
    user_value = input("Enter the value {}: ".format(user_key))
    user_dic_2[user_key] = user_value

print(user_dic_2)

user_key_search = input("Enter the key to be searched: \n")

if user_key_search in user_dic_2.keys():
    print("Yes the key is available")
else:
    print("No the key is not available")
"""
# iterate over dictionaries using for loops
"""
user_length = int(input("Enter the length of the dict: \n"))
user_dic = {}
for _ in range(user_length):
    user_key = input("Enter the key: \n")
    user_value = input("Enter the value{}: ".format(user_key))
    user_dic[user_key] = user_value

print(user_dic)

for x, y in user_dic.items():
    print("key is :", x, "and value is :", y)
"""

# print a dictionary that contains a number (between 1 and n) in the form (x, x*
"""
user_input = int(input("Enter the value of n: \n"))
user_dic = {}

\"""
here the output is {0:0, 1:1, 2:4, 3:9}
for x in range(user_input):
    user_dic.update({x: x*x})
\"""
for x in range(1, user_input+1):
    user_dic.update({x: x * x})

print(user_dic)
"""

# print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
"""
user_dic_1 = {}
for x in range(1, 16):
    user_dic_1.update({x: x*x})

print(user_dic_1)
"""
# to merge two Python dictionaries
"""
user_input_1 = int(input("Enter the length of dict1: \n"))
user_dic_1 = {}

for _ in range(user_input_1):
    user_key = input("Enter the key: \n")
    user_value = input("Enter the value{}: ".format(user_key))
    user_dic_1[user_key] = user_value

print("first user input dict is: ", user_dic_1)

user_input_2 = int(input("Enter the length of dict2: \n"))
user_dic_2 = {}

for _ in range(user_input_2):
    user_key_1 = input("Enter the key: \n")
    user_value_1 = input("Enter the value{}: ".format(user_key_1))
    user_dic_2[user_key_1] = user_value_1

print("Second user input dict is: ", user_dic_2)

#dic_3 = dict({user_dic_1: user_dic_2}) # error as unhashable type: 'dict'
user_dic_3 = {**user_dic_1, **user_dic_2}  # in case of common key , values from 2nd dict is considered
print(user_dic_3)
"""
# to sum all the items in a dictionary, -->sum of key and sum of value both
"""
user_length = int(input("Enter the length of the dict: \n"))
user_dic = {}
for _ in range(user_length):
    user_key = int(input("Enter the key value"))
    user_value = int(input("Enter the value {}:".format(user_key)))
    user_dic[user_key] = user_value

print(user_dic)

user_key_sum = 0
user_value_sum = 0

for _ in user_dic.items():
    user_key_sum = sum(user_dic.keys())

print(user_key_sum)

for _ in user_dic.items():
    user_value_sum = sum(user_dic.values())

print(user_value_sum)

user_del = int(input("Enter the key to be deleted: \n"))
if user_del in user_dic.keys():
    user_dic.pop(user_del)
    print(user_dic)
else:
    print("key not found")
"""
# to map two lists into a dictionary

# user_length_list1 = int(input("Enter the length of list1: \n"))
# user_length_list2 = int(input("Enter the length of list2: \n"))
# user_list_1 = []
# user_list_2 = []
# if user_length_list1 != user_length_list2:
#     print("Enter the length same as list 1 length")
# else:
#     while len(user_list_1) < user_length_list1:
#         user_element = input("Enter the elements for list 1: \n")
#         if user_element.isalnum():
#             user_list_1.append(user_element)
#         else:
#             print("Invalid input")
#     print(user_list_1)
#
#     while len(user_list_2) < user_length_list2:
#         user_element1 = input("Enter the elements for list 2: \n")
#         if user_element1.isalnum():
#             user_list_2.append(user_element1)
#         else:
#             print("Invalid input")
#     print(user_list_2)

"""
user_dic = []
user_dic.append(user_list_1)
user_dic.append(user_list_2)
user_dic = dict(user_dic) # length of list should be same else throws error
print(user_dic)
"""
# user_dic_1 = dict(zip(user_list_1, user_list_2))
# here if we have 1st list with length as 4 and 2nd list with length as 2, then 2nd lists' s values are replaced in dex 0,1

# print(user_dic_1)

# to get the maximum and minimum values of a dictionary.
user_length = int(input("Enter the length of the dict: \n"))
user_dic = {}
for _ in range(user_length):
    user_key = input("Enter the key for the dict: \n")
    user_value = input("Enter the value for the dict {}:".format(user_key))
    user_dic[user_key] = user_value

print(user_dic)

user_input = input("Maximum and minimum should be returned of Key or Value: \n").lower()

if user_input in ('key', 'value'):
    print("Valid input")
else:
    print("Invalid input")

if user_input == 'key':
    """
    key_max = max(user_dic.keys(), key=(lambda k: user_dic[k]))
    key_min = min(user_dic.keys(), key=(lambda k: user_dic[k]))
    print(key_max, key_min)
    """
    key_max = max(user_dic.items(), key=lambda x: x[0])
    key_min = min(user_dic.items(), key=lambda x: x[0])
    print("key max is: ", key_max)
    print("key min is: ", key_min)

if user_input == 'value':
    """
    throws error as value_max = max(user_dic.values(), key=(lambda k: user_dic[k])),KeyError: '6'-->??
    value_max = max(user_dic.values(), key=(lambda k: user_dic[k]))
    value_min = min(user_dic.values(), key=(lambda k: user_dic[k]))
    print(value_max, value_min)
    """
    value_max = max(user_dic.items(), key=lambda x: x[1])
    value_min = min(user_dic.items(), key=lambda x: x[1])
    print("Value max is: ", value_max)  # returns the key value pair
    print("Value min is: ", value_min)  # returns the key value pair
