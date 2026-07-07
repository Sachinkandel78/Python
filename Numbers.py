#There are three numeric types in Python: int, float, and complex.

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print (type(x))  # Output: <class 'int'>
print (type(y))  # Output: <class 'float'>
print (type(z))  # Output: <class 'complex'>

#int 

x = 1 
y = 35656
z = -3255522
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'int'>

#float 

x = 35e3
y =12E4
z = -87.7e100
print(type(x))  # Output: <class 'float'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'float'>

#Complex

x = 3+5j
y = 5j
z = -5j
print(type(x))  # Output: <class 'complex'>
print(type(y))  # Output: <class 'complex'>
print(type(z))  # Output: <class 'complex'>


#You can also use the int(), float(), and complex() functions to convert between numeric types:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

import random
print(random.randrange(1, 10))  # Output: A random integer from 1 to 9
