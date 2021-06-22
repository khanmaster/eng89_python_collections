# # Let's create a shopping list
# # Syntax [] - name_of_list = ["","",""]
#
# shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
#               #     0        1          2               3       4
# print(shopping_list)
# # Checking the type of this data with type()
# print(type(shopping_list))
#
# # How can access dark chocolate using the same concept that we learned yesterday INDEXING
# print(shopping_list[1]) # will display eggs -
# print(shopping_list[-1]) # lists the last item - left to right
#
# # How can I replace an item in the list
# shopping_list[0] = "mango"
# print(shopping_list)
#
# # How can we add an item to our shopping list
# shopping_list.append("Tuna")
# print(shopping_list)
#
# # Search python documentation/google and find out how could we delete nd item on index 3 from this list
#
# shopping_list.pop(3)
# print(shopping_list)
#
# # We can have multiple data types in the same list
# mix_list = [1, 2 , 3, "one", "two", "three"]
#           #  ints               string
# print(type(mix_list))

# What are Tuples and What is the diff between Lists and Tuples
# Syntax () - name_of_tuple = ("", "", "")

essentials = ("paracetamol", "Milk", "Butter")
print(essentials)
print(type(essentials))
essentials.pop(1)
print(essentials)
# Lists are MUTABLE and Tuples are IMMUTABLE






