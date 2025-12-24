#partb
#21 arithmetic operator
#a
'''a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

print("addition is: ",a+b)
print("subtraction is: ",a-b)
print("multiplication is: ",a*b)
print("division is: ",a/b)
print("modulus is: ",a%b)
print("exponentiation is: ",a**b)
print("floor division is: ",a//b)'''


#b
'''a=10
b=20
lst=[10,20,30,40]

a +=5
print("assignment operator: ",a)

print("comparison operator: ",a>b)

print("logical operator: ",a>b and b>5 )

print("identity operator: ", a is b)

print("membership operator: ",20 in lst)'''


#c
'''my_list=[20,50,10,30,60]
print(my_list)

my_list.insert(2,70)
print("my_list_after_insert: ",my_list)

my_list.remove(20)
print("my_list_after_remove: ",my_list)

my_list[1]=90
print("my_list_after_update: ",my_list)

my_list.sort()
print("my_list_after_sort: ",my_list)

my_list.reverse()
print("my_list_after_reverse: ",my_list)

for item in my_list:
    print(item)'''


#22
#a

'''marks=int(input("enter your marks: "))

if marks >75:
    print("distinction")

elif marks >=60:
    print("first cls")
    
elif marks >=50:
    print("second cls")

else:
    print("fail")'''


#b

'''for i in range(1,101):
    print(i)

    if i % 2 ==0:
        continue

    if i == 73:
        break

print(i)'''


#c
'''def is_prime(n):
    if n <=1:
        return False


    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
        
    return True

num=int(input("enter a number: "))

if is_prime(num):
    print(num,"it is a prime number")
else:
    print(num,"is not a prime number")'''
        

#23
#a

'''class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary


    def display(self):
        print("name: ",self.name)
        print("employee id: ",self.emp_id)
        print("salary is: ",self.salary)

emp1= employee("jabez",101,20000)
emp2= employee("benny",102,30000)
emp1.display()
emp2.display()'''



#b

class shape:
    def area(self):
        return 0

class circle(shape):
    def __init__(self,radius):
        self.__radius=radius
        
    def get_radius(self):
        return self.__radius

    def set_radius(self,value):
        if value >0:
            self.__radius=value
        else:
            print("radius must be positive")
            
    def area(self):
        return 3.14*self.__radius*self.__radius

c=circle(5)    


print("radius: ",c.get_radius())
print("area  of the circle: ",c.area())

c.set_radius(20)
print("updated radius: ",c.get_radius())
print("updated area  of the circle: ",c.area())

        


#c

'''with open("benny.txt","w") as f:
    f.write("jabez\n")
    f.write("is\n")
    f.write("a student\n")
    f.write("in\n")
    f.write("caddam\n")


with open("benny.txt","r") as f:
    content = f.read()
    print("the contents are: ",content)'''

    

        
        

    
          



      



      
