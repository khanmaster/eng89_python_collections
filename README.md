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
