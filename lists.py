#So today we started to learn about lists in Python. Lists are a type of data structure that can hold multiple items in a single variable. They are ordered, changeable, and allow duplicate values.

#Example of a list:
mylist = ["apple","banana", "cherry"]
print(mylist)
# output will be ['apple','banana', 'cherry']

#List allow duplicate values hai
thislist = ["apple","banana","cherry","apple", "cherry"]
print(thislist)
#o/p = ['apple', 'banana', 'cherry', 'apple', 'cherry']

# list length
print(len(thislist))
#o/p = 5

#list items-Data types 
#Example: string,int & boolean data types 
list1 = ["apple","banana", "cherry"]
list2 = [1,5,7,8,10,18,20]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
# o/p will be ['apple', 'banana', 'cherry']
#[1, 5, 7, 8, 10, 18, 20]
#[True, False, False]

#Example: A list with strings,integers and boolean values every type in one list
list5 = ["sachin",2307300,"PokharaUni",True,18]
print(list5)
#o/p will be = ['sachin', 2307300, 'PokharaUni', True, 18]
#type of variable list5 
print(type(list5))
# yo variable list5 vanni chai list datatype ko raixa o/p = <class 'list'>