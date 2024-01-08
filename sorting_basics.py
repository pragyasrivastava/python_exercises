# Bubble sort
"""
user_len_list = int(input("Enter the length of the list : \n"))
user_list = []
while len(user_list) < user_len_list:
    user_elements = int(input("Enter the elements of the list : \n"))
    if -1000<user_elements<1000:
        user_list.append(user_elements)
    else:
        print("Enter valid input")
print("user list is :\n", user_list)
for i in range(len(user_list)-1):
    for j in range(0, len(user_list)-i-1):
        if user_list[j] > user_list[j+1]:
            user_list[j], user_list[j+1] = user_list[j+1], user_list[j]

print("Sorted user list is : \n", user_list)
"""
# Insertion sort
user_len_list = int(input("Enter the length of the list : \n"))
user_list = []
while len(user_list) < user_len_list:
    user_elements = int(input("Enter the elements of the list : \n"))
    if -1000 < user_elements < 1000:
        user_list.append(user_elements)
    else:
        print("Enter valid input")
print("user list is :\n", user_list)
for i in range(1, len(user_list)):
    j = i-1
    x = user_list[i]
    while j > -1 and user_list[j] > x:
        user_list[j+1] = user_list[j]
        j -= 1
    user_list[j+1] = x

print("Sorted list is : \n", user_list)

