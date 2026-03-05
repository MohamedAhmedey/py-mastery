import random
x=int(input("Enter your first number : "))
y=int(input("Enter your second number : "))
Total=(x+y)
Product=(x*y)
Difference=(x-y)
List=[Total,Product,Difference]
Answer=random.choice(List)
print(Answer)
