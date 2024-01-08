# create a set
"""
user_length = int(input("Enter the length of the set: \n"))
user_set = set()
for _ in range(user_length):
    user_input = input("Enter the set values: \n")
    user_set.add(user_input)

print(user_set)
print(type(user_set))
"""

# To remove an item from a set if it is present in the set.
"""
user_length = int(input("Enter the length of the set: \n"))
user_set = set()
for _ in range(user_length):
    user_input = input("Enter the set values: \n")
    user_set.add(user_input)
print(user_set)

user_remove = input("Enter the element to be removed: \n")
if user_remove in user_set:
    user_set.pop(user_remove)
else:
    print("Element not available in the set given")
print(user_set)
"""
# To create an intersection, union, subset of sets.
"""
user_length_1 = int(input("Enter the length of set1: \n"))
user_set_1 = set()
for _ in range(user_length_1):
    user_input_1 = input("Enter the element of the set 1: \n")
    user_set_1.add(user_input_1)

print(user_set_1)

user_length_2 = int(input("Enter the length of the set2: \n"))
user_set_2 = set()
for _ in range(user_length_2):
    user_input_2 = input("Enter the elements of set 2 : \n")
    user_set_2.add(user_input_2)

print(user_set_2)

user_set3 = user_set_1.intersection(user_set_2)
print(user_set3)
user_set4 = user_set_1.union(user_set_2)
print(user_set4)
user_set5 = user_set_1.difference(user_set_2)
print(user_set5)
user_set6 = user_set_1.symmetric_difference(user_set_2)
print(user_set6)
user_set7 = user_set_1.issuperset(user_set_2)
print(user_set7)
"""

# to create a shallow copy of sets
"""
user_length = int(input("Enter the length of set: \n"))
user_set = set()
for _ in range(user_length):
    user_element = input("Enter the element of the set: \n")
    user_set.add(user_element)
print(user_set)

user_set1 = set(user_set)
user_set2 = user_set.copy()
print(user_set2)
user_set2.add(660)
print(user_set2)
print(user_set)
"""

# to find the maximum and minimum values in a set.
user_length = int(input("Enter the set length: \n"))
user_set = set()
for _ in range(user_length):
    user_element = input("Enter the element of the set: \n")
    user_set.add(user_element)

print(user_set)

max_value = max(user_set)
min_value = min(user_set)
print(max_value)
print(min_value)