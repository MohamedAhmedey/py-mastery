import math
"""
Docstring for Python_math
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers
"""
#Minimum and Maximum
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)
print(x)

#Power
x=pow(5,5)
print(x)

#Math.ceil rounds the number upwards to the nearest integer
#Math.floor round the number downwards to the nearest integer
x =math.ceil(2.85)
y =math.floor(2.85)
print(x)
print(y)

#Math.fabs gives the floating absolute value of a number
x=math.fabs(-100.66)
print(x)

#Math.trunc ignores the decimal part of a number
x=math.trunc(10.87)
print(x)

#Math.fmod
print(math.fmod(11,3))

#Math.frexp
print(math.frexp(12))

#math.nan(NOT A NUMBER)
print(math.nan)

#math.isnan displays TRUE if the value entered is not a real number and FALSE otherwise
print(math.isnan(math.nan))