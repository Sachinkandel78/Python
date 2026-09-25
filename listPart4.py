#Add list items
#1.Append items
#Example: using the append() method to append an item

thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
#output will be -['apple', 'banana', 'cherry', 'orange']

#2.insert items
#Example: Insert an item of the second position 
thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)
#output will be =['apple', 'orange', 'banana', 'cherry']

#3.Extend list 
#Example: add the elements of tropical to thislist
thislist=["apple","banana","cherry"]
tropical=["orange","kiwi"]
thislist.extend(tropical)
print(thislist)
#Output will be= ['apple', 'banana', 'cherry', 'orange', 'kiwi']

#4.Add any iterable
#Example: Add elements of tuples to a list
thislist=["apple","banana","cherry"]
thistuple=("kiwi","orange","pomegranate")
thislist.extend(thistuple)
print(thislist)
#Output will be = ['apple', 'banana', 'cherry', 'kiwi', 'orange', 'pomegranate']

