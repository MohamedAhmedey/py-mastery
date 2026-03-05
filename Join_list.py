Fruits =["Oranges", "apples", "Bananas", "Pineapples", "Lemons", "Grapes", "Avocados", "Tomatoes"]
Sports =["Football", "Basketball", "Volleyball", "Cricket", "Tennis", "Rugby", "Athletics", "Swimming"]
#Concatenation(Using a plus sign)
List3= Fruits+Sports
print(List3)
#Extending
Fruits.extend(Sports)
print(Fruits)
#Appending
for x in Sports:
 Fruits.append(x)
 print(Fruits)
 Fruits.append("Kiwi")
print (Fruits)