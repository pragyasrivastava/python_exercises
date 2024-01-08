# check if 1st and last element of a particular string is same and print the count for it
"""
user_length = int(input("Enter the length of string : \n"))
if user_length < 2:
    print("Enter the length to be 2 or more")
user_list = []
while len(user_list) < user_length:
    user_element = input("Enter the user input: \n")
    if user_element.isalnum() and len(user_element) <= 4:
        user_list.append(user_element)
    else:
        print("Enter only alphanumeric characters upto 4 places")
print("user entered string is :", user_list)
count = 0
for word in user_list:
    if word[0] == word[-1]:
        count = count+1

print("Same start and end characters strings are:", count)
"""
# copy a list into another list
user_length = int(input("Enter the length of list : \n"))
user_list = []
while len(user_list) < user_length:
    user_elements = input("Enter the elements of the list : \n")
    if user_elements.isalnum():
        user_list.append(user_elements)
    else:
        print("Enter valid input")

print("user list is: \n", user_list)

# Logic for copying the items in the list:
"""     
clone_list =[]
indices_to_copy = input("enter the indexes to be copied").split()  # takes input as list 
for index in indices_to_copy:
    index = int(indices_to_copy) # list cannot be passed
    clone_list = user_list[index]
print("clone_list is ", clone_list)
"""
start_index = int(input("Enter the starting index of the list to be copied: \n"))
end_index = int(input("Enter the ending index of the list to be copied: \n"))

#clone_list = user_list[start_index:end_index] -end index is not included, it takes from starting index to previous value of end _index
clone_list = user_list[start_index:end_index + 1]  # to include the end_index as well

print("clone_list is ", clone_list)
