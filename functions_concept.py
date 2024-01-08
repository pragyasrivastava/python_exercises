# function definition and calling
# def hello_world():
#     print("Hello World")
#
# hello_world()

# calling function with parameters:
# def sum(num1, num2):
#     print(num1 + num2)
#
# sum(1,2)
# sum() # throws error as sum() missing 2 required positional arguments: 'num1' and 'num2'

# defining the function with if statement -->nothing is returned if num1 or num2 are not int
# def sum(num1, num2):
#     if type(num1) is not int or type(num2) is not int:
#         return
#     return num1 + num2
#
#
# total = sum('a', 2)
# print(total)

# defining the function by passing default values for arguments
# def sum(num1=0, num2=0):
#     if type(num1) is not int or type(num2) is not int:
#         return 0
#     return num1 + num2
#
#
# total = sum(7, 2)
# print(total)

# multiple items as arguments
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("dave", "john", "sara")


# multiple named items into function
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_items(first='Dave', last='Gray')
