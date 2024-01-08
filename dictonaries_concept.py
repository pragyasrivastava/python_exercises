# Dictionaries
# band = {
#     "vocals": "Plant",
#     "guitar": "Page"
# }
#
# band2 = dict(vocals="Plant", guitar="Page")
#
# print(band)
# print(band2)
# print(type(band))
# print(len(band))
# Access items
# print(band["vocals"])
# print(band.get("guitar"))

# list all keys
# print(band.keys())

# list all values
# print(band.values())

# list of key/value pairs as tuples
# print(band.items())

# verify a key exists
# print("guitar" in band)
# print("triangle" in band)

# Change values
# band["vocals"] = "Coverdale"
# band.update({"bass": "JPJ"})
#
# print(band)

# Remove items
# print(band.pop("bass"))
# print(band)
#
# band["drums"] = "Bonham"
# print(band)

# print(band.popitem())  # tuple
# print(band)

# Delete and clear

# band["drums"] = "Bonham"
# del band["drums"]
# print(band)
#
# band2.clear()
# print(band2)
#
# del band2

# Copy dictionaries

# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# band2 = band.copy()
# band2["drums"] = "Dave"
# print("Good copy!")
# print(band)
# print(band2)

# or use the dict() constructor function
# band3 = dict(band)
# print("Good copy!")
# print(band3)

# Nested dictionaries

# member1 = {
#     "name": "Plant",
#     "instrument": "vocals"
# }
# member2 = {
#     "name": "Page",
#     "instrument": "guitar"
# }
# band = {
#     "member1": member1,
#     "member2": member2
# }
# print(band)
# print(band["member1"]["name"])

mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)
# mydict.pop()  # displays error as one argument is needed to execute the pop function
# mydict.popitem()  # removes last pair in python version 3.7 and above, below it removes arbitrary pairs
# print(mydict)

# try:
#     print(mydict["name"])
# except:
#     print("Error")
#
# for key in mydict:
#     print(key)

# for key in mydict.keys():  # keys method returns the list all the keys in the dictonaries
#     print(key)
#
# for value in mydict.values():  # value method returns the list of values in the dictonaries
#     print(value)
#
# for key, value in mydict.items():  # item method prints all keys and values
#     print(key, value)

# mydict_cpy = mydict  # direct copying so it will modify both the dict if one is modified as same address for both
# print(mydict_cpy)  # dict is unordered so does not have any particular order to store items in it
#
# mydict_cpy1 = mydict.copy()  # copy method to create dict copy
# mydict_cpy2 = dict(mydict)  # passing dict as an argument in dict method
# mydict_cpy2["email"] = "max@xyz.com"
# print(mydict_cpy2)

# # update already existing dict
# my_dict_1 = {"name": "Max", "age": 28, "city": "Boston"}
# my_dict_2 = dict(name="Mary", age=27, email="mary@xyz.com")
#
# my_dict_1.update(my_dict_2) # updating the value of dict1 with dict2
#
# print(my_dict_1) # existing key value pairs get overridden and new ones get added, non-common ones remains as it is

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

my_tuple = (8, 7)
my_dict_1 = {my_tuple: 15}
print(my_dict_1)
my_list = [1, 2]
my_dict_2 = {1: my_list}
print(my_dict_2)
my_dict_3 = {my_list: 10}
print(my_dict_3)  # throws error as list cannot pe passed as key in dict
