#Remove list items
#1.Remove specified item
#Example: Remove"banana"
thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
#output will be =['apple', 'cherry']

#what happens when more than one banana? then first occurance only remove all other remains unchanged.
thislist=["apple","banana","cherry","banana","kiwi"]
thislist.remove("banana")
print(thislist)
#output will be =['apple', 'cherry', 'banana', 'kiwi']

#2.Remove specified index
#Example: Remove the second item 
thislist=["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
#Output will be =['apple', 'cherry']

#If you dont specify the index then the pop() method removes the last item
thislist=["apple","banana","cherry"]
thislist.pop()
print(thislist)
#output will be = ['apple', 'banana']

#3.Del keyword 
thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)
#output will be =['banana', 'cherry']
#if we dont give index value all the items will be delete 
thislist=["apple","banana","cherry"]
del thislist
# print(thislist) will cause an error

#4.Clear the list
thislist=["apple","banana","cherry"]
thislist.clear()
print(thislist)
#output will be = []