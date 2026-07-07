#Boolean
print(10 > 9) #True
print(10 == 9)
print (10 < 9)   

#condition

temperature = 10
is_cold = temperature < 18
if is_cold:
   print("Wear a jacket")
else:
    print("No need to wear a jacket")

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("hello"))
print(bool(15))

#Functions can Return a Boolean
def myFunction() :
    return True
print(myFunction())

#example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#class
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Check if an object is an integer or not:
x = 200
print(isinstance(x,int))

a ="subscribe my channel"
print(a)
print(bool(a))
b=""
print(bool(b))