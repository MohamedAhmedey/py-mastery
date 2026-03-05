"""
Docstring for Error_handling
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
x=17
try:
 print(x)
except:
 print("An error has occurred")
finally:
 print("Please try again")

#raise is used to raise an exception
x=0
if x<=0:
 raise Exception("Only accepts numbers greater than zero")
print(x)

y=1000
if not type(y) is str:
 raise TypeError("Only accepts characters from a-z")
print(y)