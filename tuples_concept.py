import sys
import timeit
"""
mytuple = ("Max", 28, "Boston")  # creating tuple using parenthesis
my_tuple_1 = "Max", 28, "Boston"  # creating tuple without parenthesis
print(mytuple)
print(my_tuple_1)
print(type(my_tuple_1))

tuple_1 = ("Max")  # this acts as str not a tuple
print(tuple_1)
print(type(tuple_1))

tuple_2 = ("Max",)  # , is mandatory at the end even if only 1 element is there
print(tuple_2)
print(type(tuple_2))

# tuple creation using a list
my_new_tuple = tuple(["Max", 28, "Boston"])
print(my_new_tuple)
item = my_new_tuple[0]  # accessing element of tuple through index
print(item)
item_1 = my_new_tuple[-1]  # accessing last item
print(item_1)

#my_new_tuple[0] = "Tim"  -->error as tuple is not mutuable

for i in my_new_tuple:
    print(i)  # iterates over a tuple and prints all elements

if "Max" in my_new_tuple:
    print("yes")
else:
    print("no")

print(len(my_new_tuple))  # gives length a tuple
print(my_new_tuple.count("Max"))  # counts the number of max in the given tuple
print(my_new_tuple.index("Max"))  # returns the first index of max

my_new_tuple_1 = ('a','p','p','l','e')
my_list = list(my_new_tuple_1)  # passing a tuple into list

my_tuple = tuple(my_list)  # passing a list into tuple

# slicing of tuple

a = (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10)
b = a[2:5]
b_1 = a[:5]
b_2 = a[2:]
b_3 = a[::1]  # stepping over the tuple by 1
b_4 = a[::-1]  # reverses the tuple
"""
# unpacking a tuple
a_1 = "Max", 28, "Boston"
name, age, city = a_1 # assigning variable to each tuple element
# name, age =a_1 # throws error as variable and element count is not an exact match

# unpacking multiple elements
a_2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = a_2  # i2 returns list of elements from first index till second last
print(i2)

# comparing tuple and list
my_list_1 = [0, 1, 2, "hello", True]
my_tuple_1 = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list_1), "bytes")
print(sys.getsizeof(my_tuple_1), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)", number=1000000))