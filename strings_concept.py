# ordered , immutable and text representation

from timeit import default_timer as timer
# representation ways
# my_string = "Hello"
# my_string_1 = 'Hello'

# my_string_2 = 'I'm a programmer' -->syntax error
# my_string_2 = "I'm a programmer"
# my_string_3 = 'I\'m a programmer'
# print(my_string_3)

# my_string = """Hello World"""
# print(my_string)
# my_string_1 = """Hello\tWorld"""
# print(my_string_1)

# my_string = "Hello World"
# char = my_string[0]
# print(char)
# my_string = 'h' # overrides the value of my_string to h
# print(my_string_1)

# substring = my_string[1:5]
# print(substring)
# substring = my_string[:5]
# print(substring)
# substring = my_string[:]
# print(substring)
# my_string = my_string[::1]
# print(my_string)

# my_string = my_string[::2]
# print(my_string)

# substring = my_string[::-1]
# print(substring)

"""
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print(sentence)
for i in greeting:
    print(i)
"""

"""
# my_string = '   Hello World    '
# print(my_string)
# my_string.strip() --> does not work as strings are immutable
# print(my_string.strip())
my_string = 'Hello World'
print(my_string.upper())
print(my_string.lower())

print(my_string.startswith('Hello'))
print(my_string.endswith('Hello'))

print(my_string.find('lo'))
print(my_string.find('pp'))

print(my_string.count('o'))
print(my_string.replace('World', 'Universe'))
# print(my_string.replace('wrld', 'Universe')) --> as wrld is not there so prints the old string as it is
"""

# convert string to list
"""
my_string = 'How are you doing'
my_list = my_string.split(" ")
print(my_string)
print(my_list)

# convert list to string
new_string = ''.join(my_list)
print(new_string)
new_string_1 = ' '.join(my_list)
print(new_string_1)
"""

# my_list = ['a']*6
# print(my_list)

# bad code as time taken is large
"""
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
"""

# good code
# my_string = ''.join(my_list)
# print(my_string)

"""
my_list = ['a']*100000
start = timer()
my_string = ''

for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
"""

# formatting strings --> %, .format(), f-strings(3.6 & above)
# var = "Tom"
# my_string = "the variable is %s" % var
# print(my_string)

# var_1 = 3
# my_string = "the variable is %d" % var_1
# print(my_string)

var_2 = 3.1234567
my_string = "the variable is %f" % var_2
print(my_string)
my_string = "the variable is %d" % var_2
print(my_string)

my_string = "the variable is %.2f" % var_2
print(my_string)

var = 3.1234567
my_string = "the variable is {}".format(var)
print(my_string)
my_string = "the variable is {:.2f}".format(var)
print(my_string)

var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var_2)
print(my_string)

my_string = f" the variable is {var*2} and {var2}"
print(my_string)
