# simple append and pop in a list
"""
user_len = int(input("Enter the length of list"))
user_list = []
while len(user_list) < user_len:
    element = input("enter the elements")
    user_list.append(element)
print("user_list is : ", user_list)
remove_element = int(input("enter the index to be removed"))
remove_element1 = user_list.pop(remove_element)  # pop removes element using index position
print(user_list.pop())
"""
# list basics

mylist = ["banana", "cherry", "apples"]
print(mylist)
mylist.append("lemon")  # inserts element at last by default
print(mylist)
mylist.insert(1, "blueberry")  # inserts element at specified index
print(mylist)
item = mylist.pop()  # by default the last item is returned and removed
print(item)
print(mylist)  # list doesn't contain lemon now
mylist.remove("cherry")  # removes specific item from list
print(mylist)
# mylist.clear()  # removes all elements and returns empty list
# print(mylist)
mylist.reverse()  # prints list in reverse order
print(mylist)

mylist_1 = [4, 3, 1, -1, -5, 10]
# mylist_1.sort()  # sorts the list and values are changed in same list
print(mylist_1)

# not change the original list and sort
new_list = sorted(mylist_1)
print(new_list)

my_list_2 = [0] * 5  # adds 0 5 times to the list

my_list_3 = mylist_1 + my_list_2  # concatination of 2 lists

a = my_list_3[1:5]  # new list with elements at index from 1->5 of my_lists_3
b = my_list_3[:5]  # no start index so it goes from start to 5th index
c = my_list_3[1:]  # no end index so it goes till the last index
d = my_list_3[::1]  # step index ,by default it is one
e = my_list_3[::2]  # takes every 2nd item in the list
f = my_list_3[::-1]  # simply reverses my list

list_org = ["banana", "cherry", "apple"]
# list_cpy = list_org  #same memory is allocated
# list_cpy = list_org.copy()
list_cpy = list(list_org)  # passing list as an argument in the list function to create copy
list_cpy_1 = list[:]  # slicing to take a copy
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

# list comprehension --> advance way of creating list
my_new_list = [1, 2, 3, 4, 5, 6]
advance_list = [i * i for i in my_new_list]
print(advance_list)
