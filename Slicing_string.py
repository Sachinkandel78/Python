#You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])  # Output: 'llo'

#Slice From the Start
#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])  # Output: 'Hello'

#Slice To the End
#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])  # Output: 'llo, World!'

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:    

b = "Hello, World!"
print(b[-5:-2])  # Output: 'orl'    