#list comprehension
# Without list comprehension you will have to write a for statement with a conditional test inside:
 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
#O/P-['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[x for x in fruits if "a" in x]
print(newlist)

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
# o/p- ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']