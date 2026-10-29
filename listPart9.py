#Copy List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

#use the copy() method

thislist = ["virat", "rohit" , "sachin", "gill"]
mylist = thislist.copy()
print(mylist)
# ['virat', 'rohit', 'sachin', 'gill']


# Another way to make a copy is to use the built-in method list()
thislist = ["virat", "rohit" , "sachin", "gill"]
mylist = list(thislist)
print(mylist)

# use the slice operator
thislist = ["virat", "rohit" , "sachin", "gill"]
mylist = thislist[:]
print(mylist)

