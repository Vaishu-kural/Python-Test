#21.
#(a)
'''a=int(input("Enter First number: "))
b=int(input("Enter second number: "))
print("Addition:",a  +  b)
print("Subtraction:",a  -  b)
print("Multplication:", a  *  b)
print("Division:", a  /  b)
print("Modulus:", a  %  b)
print("Floor Division:", a  //  b)
print("Exponentiation:" ,a ** b)'''

#(b)
'''X = 50
Y =10

# Assignment Operators
x += 2
print("Assignment (x+=2):", x)

# Comparison Operators
print("x > y:", x > y)

# Logical Operators
print("(x > 5) and (y < 10):", (x > 5) and (y < 10))

# Identity Operators
print("x is y:", x is y)

# Membership Operators
lst = [1, 2, 3, 4]
print("2 in list:", 2 in lst)
'''
#C)
'''
fruits = ["apple", "banana", "cherry", "mango", "grapes"]
fruits.append("orange")
fruits.insert(2, "kiwi")
fruits.remove("banana")
fruits[0] = "pineapple"
fruits.sort()
fruits.reverse()
for item in fruits:
    print(item)
'''
#22. A).
'''marks = int(input("Enter marks: "))
if marks >= 75:
    print("Distinction")
elif m >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")'''
#B).

'''for i in range(1, 101):
    if i % 2 == 0:
        continue
    if i == 73:
        break
    print(i)'''

#C).
'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter number: "))
print(is_prime(num))'''
#23.
#(A)
'''
class Employee:
    def _init_(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)

e1 = Employee("Arun", 5, 50000)
e2 = Employee("Esakki", 8, 60000)
e1.display()
e2.display()'''

#B).
'''class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def _init_(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def get_radius(self):
        return self.__radius

    def set_radius(self, r):
        self.__radius = r

c = Circle(10)
print("Area:", c.area())
print("Radius:", c.get_radius())'''

#C).
'''
try:
    n = float(input("Enter a number: "))
    print("Result:", 100 / n)

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    print("Program completed.")'''

