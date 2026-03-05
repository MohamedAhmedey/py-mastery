Num1=float(input("Enter the first number : "))
operator=input("Enter the operator: ")
Num2=float(input("Enter the second number : "))
if operator=="+":
    print("Answer is : ", Num1+Num2)
elif operator=="-":
    print("Answer is : ", Num1-Num2)
elif operator=="*":
    print("Answer is : ", Num1*Num2)
elif operator=="/" and Num1 or Num2 !=0:
    print("Answer is : ", Num1/Num2)
elif Num1 or Num2==0:
    print ("Error occurred. Not possible to divide a number by 0")
elif operator=="**":
    print("Answer is : ", Num1**Num2)
elif operator=="//":
    print("Answer is : ", Num1//Num2)
else:
    print("Invalid operator")


