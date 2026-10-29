#Sort list

thislist = [100,50,99,2,56]
thislist.sort()
print(thislist)
# o/p- [2, 50, 56, 99, 100]

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# sort the list alphabetically
thislist = ["ram", "sachin", "angell", "krips" ]
thislist.sort()
print(thislist)
# o/p- ['angell', 'krips', 'ram', 'sachin']

# sort the list numerically

thislist = [100,50,99,2,56]
thislist.sort()
print(thislist)
# o/p- [2, 50, 56, 99, 100]

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

thislist = ["orange","banana","apple","cherry"]
thislist.sort(reverse= True)
print(thislist)
# ['orange', 'cherry', 'banana', 'apple']

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["orange","Banana","apple","Cherry"]
thislist.sort()
print(thislist)
#o/p- ['Banana', 'Cherry', 'apple', 'orange']
# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["orange","Banana","apple","Cherry"]
thislist.sort(key= str.lower)
print(thislist)
# o/p- ['apple', 'Banana', 'Cherry', 'orange']

# Reverse order
# What if you want to reverse the order of a list, regardless of the alphabet?
thislist = ["orange","banana","apple","cherry"]
thislist.reverse()
print(thislist)
#o/p- ['cherry', 'apple', 'banana', 'orange']