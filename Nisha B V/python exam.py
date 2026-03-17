'''#21 a)Arithmetic Operators
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
print("Floor Division:",a // b)
print("Exponent:",a**b)'''

'''#21 b)All other Opperators
a = 10
b = 5
c = a
print("Assignment:",c)
print("a>b:",a>b)
print("a == b:",a == b)
print("Logical AND:",a>5 and b< 10)
print("a is b:", a is b)
list1 = [1,2,3,4,5]
print("3 in list:",3 in list1)'''

'''#21 c)List Operations

list1 = [10,20,30,40,50]
list1.insert(2,25)
list1.remove(40)
list1[0] = 15
list1.sort()
list1.reverse()
for i in list1:
    print(i)'''

'''#22 a) Conditional Statements

marks = int(input("Enter marks:"))
if marks> 75:
    print("Distinction")
elif marks>=60:
    print("First Class")
elif marks>=50:
    print("Second Class")
else:
    print("Fail")'''

'''#22 b)Loop with  Flow Control

for i  in range(1,101):
    if i % 2==0:
        continue
    if i == 73:
       break
pass
print(i)'''

'''#22 c) User Defined Function (prime number)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n% i==0:
            return  False
        return True
num = int(input("Enter a number:"))
if is_prime(num):
     print("Prime Number")
else:
     print("Not Prime Number")'''

'''#23 (or)

file = open("sampel.txt","w")

for i in range(1,6):
    line = input("Enter line:")
    file.write(line + "\n")
    
file.close()

file = open("Sample.txt","r")

print("Contents  of the file:")
for line in file:
    print(line)
    
file.close()'''
        


