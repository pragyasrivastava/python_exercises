import copy

# copy using '=' operator
"""
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
print('ID of Old List:', id(old_list))
print('ID of New List:', id(new_list))
new_list[2][2] = 9
print('New List:', new_list)
print('ID of New List:', id(new_list))
print('Old List:', old_list)
print('ID of Old List:', id(old_list))
"""

# copy using copy operator --> shallow copy
"""
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = old_list.copy()
print('ID of Old List:', id(old_list))
print('ID of New List:', id(new_list))
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)
"""
# shallow copy with nested object
"""
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = old_list.copy()
old_list[1][1] = 'AA'  # as same nested objects is shared so this change affects both lists

print("Old list:", old_list)
print("New list:", new_list)
"""

# deep copy
"""
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
"""

# different ways to copy list without copy() method
user_list = [1, 2, 3, 4, 5]
new_list = user_list[:]
print("new list using list slicing is : ", new_list)

user_list_1 = ['abc', 'xyz', 'def']
new_list_1 = []
new_list_1.extend(user_list_1)
print("new list using extend function is: ", new_list_1)