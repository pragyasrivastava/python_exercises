# sets : unordered, mutuable and no duplicates
"""
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4)) # set using constructor

print(nums)
print(nums2)
print(type(nums))
print(len(nums))


# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
"""
# myset = {1, 2, 3}
# my_set_1 = {1, 2, 3, 1, 4}
# print(myset)
# print(my_set_1)

# my_set_2 = set("Hello")
# print(my_set_2)  # takes each character of hello and creates the set, trick to find how many characters are there in the word
# my_set_3 = {}  # creates an empty dict
# print(type(my_set_3))
# my_set_4 = set()
# my_set_4.add(1)
# my_set_4.add(2)
# my_set_4.add(3)
# my_set_4.remove(3)
# my_set_4.remove(4)  # throws key error as element not available
# my_set_4.discard(2)
# my_set_4.discard(4)  # doesn't throw any error
# my_set_4.clear()  # returns empty set
#my_set_4.pop()  --> removes arbitrary element from the set
#print(my_set_4.pop() -->returns the element removed arbitrary from the set
#print(my_set_4)
"""
for i in my_set_4:
    print(i)

if 1 in my_set_4:
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)  # this unions odds and even sets without duplicates
print(u)

i = odds.intersection(evens)  # this returns set with common elements between the passed sets, empty set in case of no common element
print(i)

i1 = odds.intersection(primes)
print(i1)

i2 = evens.intersection(primes)
print(i2)
"""

#setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#setB = {1, 2, 3, 10, 11, 12}

#diff = setA.difference(setB)  #diff function will return a new set with all the values of setA that are not in the passed setB
#print(diff) #o/p--> {4, 5, 6, 7, 8, 9}

#diff_1 = setA.symmetric_difference(setB) #this returns a new set with all the unique values in both sets
#print(diff_1)

#setA.update(setB) #setA is updated with all unique values from setB
#print(setA)

#setA.intersection_update(setB) #setA is updated only with common values in both setA and setB
#print(setA)

#setA.difference_update(setB) #this returns the values which are unique in setA and discards all values which are common in both setA & setB
#print(setA)

#setA.symmetric_difference_update(setB) # returns all the values which are unique in both setA and setB
#print(setA)

# setC = {1, 2, 3, 4, 5}
# setD = {1, 2, 3}
# setE = {7,8}
#
# print(setC.issubset(setD))
# print(setD.issubset(setC))
#
# print(setC.issuperset(setD))
# print(setD.issuperset(setC))
#
# print(setC.isdisjoint(setD))
# print(setD.isdisjoint(setE))

#copying sets
"""
setC = setD
setD.add(8)
print(setC)
print(setD)
"""

# #setD = setC.copy()
# setD = set(setC)
# setD.add(9)
# print(setD)
# print(setC)

a = frozenset((1, 2, 3, 4))
b = {9, 10}
print(a.union(b))

#a.add(1)  # throws error as frozen sets are immutuable they cannot be changed once created
#a.remove(1) #throws error as frozen sets are immutuable they cannot be changed once created