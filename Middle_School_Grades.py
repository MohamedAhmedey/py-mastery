#Write a program to generate remarks for awarding middle school children. Use your own remarks(at least 4) based on 4 subjects
#Allow the users to enter individual subject marks. Marks should be in pure integer form or pure numbers
#The grading depends on the total marks
#Find(Total marks,Average)

Arts=int(input("Enter the marks for arts : "))
Home_science=int(input("Enter the marks for Home Science : "))
Agriculture=int(input("Enter the marks for Agriculture : "))
Maths=int(input("Enter the marks for Maths : "))
Total= Arts+Home_science+Agriculture+Maths
Average=(Arts+Home_science+Agriculture+Maths)/4
if Total >=350:
    print("Exceeding expectation")
elif Total >=300:
    print("Above expectation")
elif Total >200:
    print("Meeting expectation")
else:
    print("Below expectation")
print("The Average is :",(Average))
print("The total is :",(Total))


