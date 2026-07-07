x = 15
y = 4
#Arithmetic operators
print("The sum is :",x+y)
print("Subtraction:",x-y)
print("Multiplication is :",x*y)
print("Division is :",x/y)
print("Modulus",x%y)
print("Exponentiation",x**y)
print("Floor Division",x//y)


#Assignement operators
a = 10
a += 5
print("The value of a is :",a)
b = 20
b -= 5
print("The value of b is :",b)
c = 5
c *= 2
print("The value of c is :",c)
d = 10
d /= 2      
print("The value of d is :",d)

#comparison operators
p = 10
q = 20
print("Is p equal to q?",p==q)
print("Is p not equal to q?",p!=q)
print("Is p greater than q?",p>q)
print("Is p less than q?",p<q)
print("Is p greater than or equal to q?",p>=q)
print("Is p less than or equal to q?",p<=q)


#ternery operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print("The status is :", status)

#Logical operators
x =5
y = 10
print(x>0 and y>0) #True
print("x is greater than 0 or y is greater than 0?",x>0 or y>0) #True
print("not (x > 0 and y > 0)",not (x>0 and y>0)) #False


#Bitwise operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print("Bitwise AND (a & b):", a & b)  # Output: 1 (0001 in binary)
print("Bitwise OR (a | b):", a | b)   # Output: 7 (0111 in binary)
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010
print(6 & 3)

