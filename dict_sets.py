# Dictionaries and Sets both are Data collections in Python
## Dict?
### Sets?

# Dict are another way to manage data but can be a little more Dynamic
# Dict work as a KEY AND VALUE
# KEY = THE REFERENCE OF THE OBJECT
# VALUE = WHAT THE DATA STORAGE MECHANISM YOU WISH TO USE
# Dynamic as it we have Lists, and another dict inside a dict
# Syntax - name = {}  we use {} brackets to declare a Dict
#          key  = value

# key
# students_1 = {
#     "name": "James",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]
# }                                #   0              1                2               3
# # Let's check if we have got the syntax right and print the dict
# # print(students_1)
# # print(type(students_1))
# print(students_1["stream"])# This is how we can fetch the value saved in the key called stream in our dict
# print(students_1["completed_lessons_names"][1])
#
# # Could we apply CRUD on a Dict
# # print the second last index of key completed_lessons_names:[]
# # How can we change the value of any key in our dict
# students_1["completed_lessons"] = 3
# print(students_1["completed_lessons"])
#
# # Let's see how can we remove an item from our completed lessons names
# students_1["completed_lessons_names"].remove("operators")
# print(students_1["completed_lessons_names"])
#
# # We have some builtin methods that we can use with dict
# # To print all the keys keys()
# print(students_1.keys())
#
#
# # To print all the values only values()
# print(students_1.values())

# Set are also Data collection
# Syntax name = {"", "", ""}
# What is the diff between sets and dict
# Sets are unordered
shopping_list = ["eggs", "tea", "milk"]
              #    0       1      2
print(shopping_list)

car_part = {"Engine", "Wheels", "Windows"}
print(car_part)
# Can we add anything to a set
car_part.add("seats")
print(car_part)

# can we remove an item
car_part.discard("Wheels")
print(car_part)






