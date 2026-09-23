# Accessing List Items
#Example: Print the second item of the list 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Output will be banana

#Negative Indexing
#Example: Print the last item in the list 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#output will be cherry paxadi bata suru hunxa negative indexing ma

#Range of Indexes
#Example: Return the third,fourth and fifth items
thislist = ["apple","banana","cherry", "orange", "kiwi", "mango"]
print(thislist[2:5])
#output will be :L ['cherry','orange','kiwi'] 5 not included only 2,3,4 included

#Example:this example returns the items from the beginning to but not including "kiwi"
thislist = ["apple","banana","cherry", "orange", "kiwi", "mango"]
print(thislist[:4])
#output will be :['apple', 'banana', 'cherry', 'orange']

#Example: This example returns the items from "cherry" to end
thislist = ["apple","banana","cherry", "orange", "kiwi", "mango"]
print(thislist[2:])
#Output will be :['cherry', 'orange', 'kiwi', 'mango'] start range value is given as 2 but ending isnot given so it covers all after the starting point

#Range of the negative indexes 
thislist = ["apple","banana","cherry", "orange", "kiwi", "mango"]
print(thislist[-4:-1])
#output will be ['cherry', 'orange', 'kiwi']

#Check if item exists
thislist = ["apple","banana","cherry", "orange", "kiwi", "mango"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruits list")
#output will be :Yes,'apple' is in the fruits list