#Python Test
#21.a)Arithmetic operators
a= int(input("Enter num1:"))
b= int(input("Enter num2:"))
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modules:", a%b)
print("Exponentiation:",a**b)

#b)All other operatiors
#(assignment, comparison, logical, identity and membership)
x = 30
y = 10
lst = [10,20,30]
#Assignment operator
x += 5
print("Assignment: (x += 5):", x )
#Comparison operator
print("x==y:",x==y)
print("x>y:",x>y)
#logical operator
print("x>y and y<12:", x>y and y<12)
#identity operator
print("x is y:", x is y)
print("x is not y:", x is not y)
#membership operator
print("10 in list:", 10 in lst)
print("50 not in list:", 50 not in lst)

#C)list operators
lst= [6,5,2,8,1]
print("original:",lst)
#insert
lst.insert(2,10)
print("After insert:",lst)
#delete
lst.remove(5)
print("After remove:", lst)
#update
lst[1]=36
print("After update:", lst)
#sort
lst.sort()
print("sorted:", lst)
#Reverse
lst.reverse
print("reversed:", lst)
#loop
for item in lst:
    print("item:",item)

#22.a)Conditional Statements
marks= int(input("Enter marks:"))
if marks > 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")

#b)Loops with flow control
for i in range(1,101):
    if i%2==0:
        print(i)
        continue
    elif i==73:
        print(i)
        break
    else:
        print("end")

#c)User undefined funtions
def is_prime(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
num= int(input("Enter number:"))
print("Prime:", is_prime(num))

#23.a)Class and Object
class Employee:
    def __init__(self,name,emp_id,salary):
        self.name= name
        self.emp_id= emp_id
        self.salary= salary


    def display(self):
        print("Name:",self.name)
        print("ID:",self.emp_id)
        print("Salary:", self.salary)

emp1= Employee("Sanmati",1001,30000)
emp2= Employee("Sanjana",1002,35000)

emp1.display()
emp2.display()

'''#b)Inheritence
class Shape:
    def __init__(self,color):
        self.color= color
        
    def display(self):
        print("color:",self.color)

class Circle(Shape):
    def __init__(self,color,radius):
        Shape._init_(self,color)
        self.raduis=radius
        
    def display(self):
        Shape.display(self)
        print("Radius:",self.radius)
        
circle= Circle("Yellow",5)
circle.display()'''

#c) Exception Handling
try:
    num=int(input("Enter a number:"))
    result=100/num
    print("result")
except ValueError:
     print("Invalid input")
except ZeroDivisionError:
     print("Cannot devide by zero")
finally:
    print("Execution complete")'''
                
            
           
        
       
        


        
    



    














        

    
    
    











    
     
   

               
                     
                   
                   
               
    
          
           
                       
           
           

           













           
















