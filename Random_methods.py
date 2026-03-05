import random
Fruits =["Oranges", "Apples", "Bananas", "Pineapples", "Lemons", "Grapes", "Avocados", "Tomatoes"]

#shuffle reorganoises a sequence of items
x=random.shuffle(Fruits)
print(Fruits)

#choice enables you to display one random item form a list
x=random.choice(Fruits)
print(x)

#sample returns random specified number of items from a sequence
x=random.sample(Fruits,k=4)
print(x)