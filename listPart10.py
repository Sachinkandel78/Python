# #Join list

# # Join two list. One of the easiest ways are by using the + operator
# list1 = ["a","e","i"]
# list2 = [1,2,3]
# list3 = list1 + list2
# print(list3)
# # o/p - ['a', 'e', 'i', 1, 2, 3]

# # Another way to join two lists is by appending all the items from list2 into list1, one by one:
# list1 = ["a","e","i"]
# list2 = [1,2,3]
# for x in list2:
#     list1.append(x)

# print(list1)
# #  output same as above

# Or we can use the extend() method, where the purpose is to add elements from one list to another list:

list1 = ["a","e","i"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)