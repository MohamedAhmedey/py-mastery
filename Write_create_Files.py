with open("Oranges.txt","a") as F:
    F.write(input("Add your own data : "))
with open("Oranges.txt","r") as F:
    print(F.read())
f=open("New_file","x")