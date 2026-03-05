"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
"""
x=["Books","Pencils","Pens"]
y=["Books","Pencils","Pens"]
z=y
print(y is z)
#Answer is true becuse they are sharing the same memory location
print(x is y)
#The answer is false because x is not the same object as y/ do not share the same memory location
print(x==y)
#Answer is true because == Checks if the values of both variables are equal

#The is not operator returns True if both variables do not point to the same object
print(x is not y)
print(z is not y)
print(x!=z)