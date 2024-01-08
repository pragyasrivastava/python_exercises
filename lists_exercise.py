users = ['Dave', 'John', 'Sara']  # list with similar data type

data = ['Dave', 42, True]  # list with different data types

emptylist = []

print("Dave" in emptylist)  # returns boolean output : False

print(users[0])  # returns list item at 0th index
print(users[-2])  # returns item at last index

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')  # adding new item to existing list
print(users)

users += ['Jason'] # adding new list to existing list
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')  # adding Bob at 0th position in users list
print(users)

users[2:2] = ['Eddie', 'Alex']  # no list slicing as start and end position is same
print(users)

users[1:3] = ['Robert', 'JPJ']  # list slicing happens here and 1st ,2nd position values are replaced
print(users)

users.remove('Bob')  # remove items from list
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data -- deletes the list completely
data.clear()  # keeps the list and clear the data inside it
print(data)

users[1:2] = ['dave']
users.sort()  # sorting happens for capital letters then small letters
print(users)

users.sort(key=str.lower)
print(users)  # include lowercase letters in alphabetical sorting

nums = [4, 42, 78, 1, 5]
nums.reverse()  # reverse the list
print(nums)

# nums.sort(reverse=True) -- sort the list in descending order
# print(nums)

print(sorted(nums, reverse=True))  # Global sorting function
print(nums)

# creating copy of existing list
numscopy = nums.copy()  # using copy function
mynums = list(nums)  # using constructors
mycopy = nums[:]  # using list slicing

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)  # original list remains as it is

print(type(nums))  # to know data type of list

mylist = list([1, "Neil", True])  # creating list using constructors
print(mylist)


