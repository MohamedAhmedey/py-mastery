"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
"""
Fruits =["Oranges", "apples", "Bananas", "Pineapples", "Lemons", "Grapes", "Avocados", "Tomatoes"]
for x in Fruits:
    print(x)
for x in "mohamed":
    print(x)
#break keyword stops the loop at the specified point
for x in "python":
    print(x)
    if x=="t":
        break
#continue stops current iteration and continues with the next/skips the specified item
for x in "python":
   if x=="h":
       continue
   print(x)
#pass keyword enables one to have an incomplete loop
   for x in "coding":
       pass
#Nested loops are loops within other loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
amt = ["Ten","Three","Twenty"]
for x in adj:
  for y in fruits:
    for z in amt:
        print(z, x, y)












