"""
List([])
Tuple(())
Set({})
"""
#python list
#Indexing begins with the number 0 and not 1
Fruits =["Oranges", "Apples", "Bananas", "Pineapples", "lemons", "Grapes", "Avocados", "Tomatoes"]
print(Fruits[0])
#Slicing
print(Fruits[0:6])
print(Fruits[0:5])
"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets
List items are ordered, changeable/mutable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
If you add new items to a list, the new items will be placed at the end of the list
The list is changeable/mutable, meaning that we can change, add, and remove items in a list after it has been created
Since lists are indexed, lists can have items with the same value
"""
print("The list has :", len(Fruits),"items")
print(type(Fruits))
#Negative indexing
print(Fruits[-4:-1])
print(Fruits[-4:])
print(Fruits[ :4])
