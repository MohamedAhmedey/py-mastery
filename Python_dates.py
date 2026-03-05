import datetime
#datetime.date.today displays the current date
x=datetime.date.today()
print(x)

#datetime.datetime.now displays the current date and time
x=datetime.datetime.now() 
print(x)

#Day of the week
print(x.day)
print(x.strftime("%b"))
