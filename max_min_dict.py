# to get the maximum and minimum values of a dictionary.
user_length_1 = int(input("Enter the length of the dict: \n"))
user_dic = {}
for _ in range(user_length_1):
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
    key_max = max(user_dic.keys(), key=lambda x: x[0])
    key_min = min(user_dic.keys(), key=lambda x: x[0])
    print("key max is: ", key_max)
    print("key min is: ", key_min)

    """
    key_max = max(user_dic.items(), key=lambda x: x[0])
    key_min = min(user_dic.items(), key=lambda x: x[0])
    print("key max is: ", key_max)
    print("key min is: ", key_min)
    """
if user_input == 'value':
    # throws string index out of range error-->??
    # value_max = max(user_dic.values(), key=lambda x: x[1])
    # value_min = min(user_dic.values(), key=lambda x: x[1])
    value_max_key = max(user_dic, key=user_dic.get) # this returns the key which has maximum value
    value_min_key = min(user_dic, key=user_dic.get)
    max_value = user_dic[value_max_key]  # returns the maximum value
    min_value = user_dic[value_min_key]
    print("Value max is: ", max_value)
    print("Value min is: ", min_value)

    """
    value_max = max(user_dic.items(), key=lambda x: x[1])
    value_min = min(user_dic.items(), key=lambda x: x[1])
    print("Value max is: ", value_max)  # returns the key value pair
    print("Value min is: ", value_min)  # returns the key value pair
    """
