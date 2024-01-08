# Remove elements in list at a particular index
"""
user_len = int(input("Enter the length of list"))
user_list = []
while len(user_list) < user_len:
    element = input("enter the elements")
    user_list.append(element)
print("user_list is : ", user_list)
# for index and value
for index, value in enumerate(user_list):
    print(index, value)
del_index = int(input("Enter the index to be deleted"))
#print(type(del_index))
if 0 <= del_index < len(user_list):
    remove_element = user_list.pop(del_index)
#remove_element1 = user_list.remove(del_index)
print('user list is: ', user_list)
"""
# Remove duplicates from list
"""
user_length = int(input("Enter the length : \n"))
user_list = []
while len(user_list) < user_length:
    user_element = int(input("Enter the elements : \n"))
    if -1000 < user_element < 1000:
        user_list.append(user_element)

print("User entered list is : ", user_list)

for i in range(len(user_list)):
    for j in range(i+1, len(user_list)):
        if user_list[i] == user_list[j]:
            user_list.pop(j)
            break

print("New list after removing duplicates: ", user_list)
print(user_list)
"""
# remove duplicates using set
"""
user_length = int(input("Enter length of list"))
user_list = []
while len(user_list) < user_length:
    user_element = input("Enter the element")
    if user_element.isalnum():
     user_list.append(user_element)
    else:
       print("Invalid input")
print("User entered list is : \n", user_list)

uniq_set = set(user_list)
uniq_list = list(uniq_set)
print("Unique list is : \n", uniq_set)
"""

# check if list is empty

while True:
    user_list = input("Enter the elements of the list")
    if not user_list:
        print("List is empty")
        break
    else:
        print("list is not empty")