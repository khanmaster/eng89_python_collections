- How to create a new project in Pycharm
`click on file` then `new project` then `enter name` click `create`

# Python Data Collections
- Lists
- Tuples
- Dict
- Sets

- Lists (AKA array in other languages)

- Shopping list - multiple items
- add, edit, delete, update
- What is `CRUD` - `Create` `Read` `update` and `delete`
```python 
shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
              #     0        1          2               3       4
print(shopping_list)
# Checking the type of this data with type()
print(type(shopping_list))

# How can we access dark chocolate using the same concept that we learned yesterday INDEXING
print(shopping_list[1:4]) # will display eggs -
print(shopping_list[-1]) # lists the last item - left to right

# How can we replace an item in the list 
shopping_list[0] = "mango"
print(shopping_list)

# How can we add an item to our shopping list
shopping_list.append("Tuna")
print(shopping_list)
```
- Search python documentation/google and find out how could we delete nd item on index 3 from this list
- List with multiple data types


#### What are Tuples and What is the diff between Lists and Tuples
`Syntax () - name_of_tuple = ("", "", "")`
```python


essentials = ("paracetamol", "Milk", "Butter")
print(essentials)
print(type(essentials))
essentials.pop(1)
print(essentials) # this would throw an error as Tuples are IMMUTABLE
# Lists are MUTABLE and Tuples are IMMUTABLE
```
#### Dictionaries and Sets both are Data collections in Python
```python
students_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]
}                                #   0              1                2               3
# Let's check if we have got the syntax right and print the dict
# print(students_1)
# print(type(students_1))
print(students_1["stream"])# This is how we can fetch the value saved in the key called stream in our dict
print(students_1["completed_lessons_names"][1])

# Could we apply CRUD on a Dict
# print the second last index of key completed_lessons_names:[]
# How can we change the value of any key in our dict
students_1["completed_lessons"] = 3
print(students_1["completed_lessons"])

# Let's see how can we remove an item from our completed lessons names
students_1["completed_lessons_names"].remove("operators")
print(students_1["completed_lessons_names"])

# We have some builtin methods that we can use with dict
# To print all the keys keys()
print(students_1.keys())


# To print all the values only values()
print(students_1.values())
```
#### Set are also Data collection
- Syntax name = {"", "", ""}
- What is the diff between sets and dict
- Sets are unordered
```python
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
```