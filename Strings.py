print("Hello")
print('Hello')

#Quotes inside a quotes
print("He is called 'Johnny'")

#Assignment of a string to a variable
a = "Hello"
print(a)

#string are arrays
a = "Hello, World!"
print(a[1])  # Output: 'e'
print(a[5])  # Output: 'o'

#Looping through a string
for x in "banana":
    print(x)

#String length
a = "Hello, World!"
print(len(a))  # Output: 13

#Check string
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)


#string concatenation
a = "hell0"
b = "world"
c= a + " " + b
print(c)  # Output: 'hello world'


#string format
age = 18
txt = f"My name is sachin, and I am {age}"
txt1 = f"My name is sachin, and I am {4+age}"
print(txt)
print(txt1)

#Escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#String methods
a = "hello, World!"
print(a.upper())  # Output: 'HELLO, WORLD!'
print(a.lower())  # Output: 'hello, world!'
print(a.strip())  # Output: 'Hello, World!'
print(a.replace("H", "J"))  # Output: 'Jello, World!'
print(a.split(","))  # Output: ['Hello', ' World!']
print(a.capitalize())  # Output: 'Hello, world!'

for x in "banana":
    print(x)
