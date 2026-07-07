#Python variables are used to store data in a program. They can hold different types of data, such as numbers, strings, lists, and more. Here are some examples of how to use variables in Python:

x = 5  # This is an integer variable
y = "Sachin"  # This is a string variable
print(x)
print(y)

#Casting is used to convert one data type to another. For example, you can convert a string to an integer or a float to an integer. Here are some examples of casting in Python:

a = "10"
b = int(a)  # Convert string to integer
print(b)    

x = str(3)  # Convert integer to string
y = int(3.14)  # Convert float to integer
z = float(3)  # Convert integer to float
print(x)    
print(y)    
print(z)    

#Get the data type of a variable using the type() function
print(type(x))
print(type(y))
print(type(z))  

#Assign multiple variables at once
x,y,z = "orange","banana","cherry"
print(x)
print(y)
print(z)    


#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"   

  myfunc()

print("Python is " + x)
