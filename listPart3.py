#Change list items
#Change the item value
#Example: Change the second item 
thislist=["apple","banana","cherry"]
thislist[1]="blackcurrant"
print(thislist)
#output will be ['apple', 'blackcurrant', 'cherry']

#Example: Change the values "banana" and "Cherry" with the values "blackcurrent"n and "watermelon"
thislist=["apple","banana","cherry","orange","kiwi"]
thislist[1:3]=["blackcurrent","watermelon"]
print(thislist)
#output will be ['apple', 'blackcurrant', 'cherry']

#Example: Change the second value by replacing it with two new value
thislist=["apple","banana","cherry"]
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)
#Output will be ['apple', 'blackcurrant', 'cherry']

thislist=["apple","banana","cherry"]
thislist[1:3]=["watermelon"]
print(thislist)
#Output will be ['apple', 'watermelon']

#Insert items
#Example:Insert"watermelon"as the third item
thislist=["apple","banana","cherry"]
thislist.insert(2,"watermelon")# index 2 ma watermelon vanney item hala(insert)gara
print(thislist)
#Output will be ['apple', 'banana', 'watermelon', 'cherry']