#Loop lists
#1.Loop through a list
#Example: Print all items in the list one by one
thislist=["apple","banana","cherry","kiwi"]
for x in thislist:
    print(x)
###output will be 
#apple
#banana
#cherry
#kiwi

#2.Loop through the indexed numbers
#Example: Print all items by referring to the index number
thislist=["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# output will be
#apple
#banana
#cherry 
thislist=["apple","banana","cherry"]
for i in range(2):
    print(thislist[i])
# output will be
#apple
#banana

#3.Using a while loop 
#Example: Print all item using a while loop to go through all the indexed numbers
thislist=["pomegranate","apple","banana","cherry",]
i=0
while i< len(thislist):
    print(thislist[i])
    i=i+1
"""output will be:
pomegranate
apple
banana
cherry"""

#4. Looping using list comprehension
#Example: A short hand for loop that will print all items in a list

thislist=["kera","apple","banana","cherry"]
[print(x) for x in thislist]

"""output will be 
kera
apple
banana
cherry
"""