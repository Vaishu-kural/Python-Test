
#1
class car:
    '''brand="Toyota"
    color="red"
My_car=car()
print("brand:",My_car.brand)
print("color:",My_car.color)'''
#2
    '''class phone():
   def __init__(self,brand,price,ram):
       self.brand=brand
       self.price=price
       self.ram=ram
   def display(self):
       print("Brand:",self.brand)
       print("Price:",self.price)
       print("ram:",self.ram)
oppo=phone("Oppo","150000","16gb")
vivo=phone("Vivo","20000","8gb")
oppo.display()
vivo.display()'''
#3
'''class phone():
    Changetype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
oppo=phone("oppo","150000","16gb")
vivo=phone("viv","20000","8gb")
oppo.display()
vivo.display()'''
#Dictionaries
'''student = {
    "name":"john",
    "age":20,
    "course":"python"
}
print(student["name"])
print(student["age"])
#Add new key-value
student["city"] = "chennai"
#Update value
student["age"] = 21
#Delete a key
del student["course"]
#print entire dictionary
print(student)'''
#4
'''student = {
    "student1": {
        "name":"Alice",
        "age":20
    },
    "student2": {
        "name":"mano",
        "age":22
      }
    }

print(student["student1"]["name"])
print(student["student1"]["age"])'''
#5
#Encapsulation

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
# Object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # ❌ Error: Cannot access private variable directly'''



'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get__balance(self):
        return self.__balance


# Runtime input
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(initial_balance)

deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

print("Final Balance:", account.get_balance())'''

'''#Polymorphism

class Dog:
    def sound(self):
        return "Bow"

class Cat:
    def sound(self):
        return "Meow"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())'''


'''# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   # Only idea, no implementation

# Car must implement start()
class Car(Vehicle):
    def start(self):
        print("Car engine starts with a key")

# Bike must implement start()
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self start button")

# Using abstraction
v1 = Car()
v2 = Bike()
v1.start()
v2.start()'''

'''#Inheritance
#parent class
class Animal:
    def sound(self):
      print("Animals make different sounds")
#child class (inherits from Animal
class Dog(Animal):
    def sound(self):
      print("Woof! Woof!")
class Cat(Animal):
    def sound(self):
      print("meow!")
#Objects
dog1 = Dog()
cat1 = Cat()
dog1.sound() #Output: Woof! Woof!
cat1.sound() #Output: Meow'''



                 '''PART A
                   
 What is the correct file extension for Python files?
A) .pyth		B) .pt	C) .python	D) .py
Ans : D).py

2. Which function is used to display output in Python?
A) input()	B) display()	C) output()	D) print()
Ans : D) print()

3. Which of the following is a valid variable name in Python?
A) 2name	B) user-name	C) user_name	D) user name
Ans : C) user_name

4. Which of the following is a comment in Python?
A) // This is a comment		B) /* This is a comment */
C) # This is a comment		D) <-- This is a comment -->
Ans : C) # This is a comment

5. What is the output of: print(type(10.5))
A) <class 'int'>	B) <class 'float'>	C) <class 'str'>	  D) <class 'double'>
Ans : B) <class’float’>

6. Which operator is used for exponentiation in Python?
A) ^	B) **	C) %	D) //
Ans : B) **

7. How do you access the second item in a list named fruits = ["apple", "banana", "cherry"]?
A) fruits[2]	B) fruits(1)	C) fruits[1]	D) fruits[0]
Ans : B) fruits(1)

8. Tuples are:
A) Mutable	B) Immutable	     C) Changeable		D) Not iterable
Ans : B) Immutable

9. Which keyword is used to check membership in a list or tuple?
A) contains	B) exist	C) in	D) has
Ans : C) in

10. What is the output of len({1, 2, 3, 3})?
A) 3	B) 4	C) 5	D) Error
Ans : B)4

11. Which of the following methods is used to access all keys in a dictionary?
A) .values()	B) .keys()	C) .get()	D) .all()
Ans : B).key()

12. Which of the following is the correct syntax for an if-else statement?
A) if x > 10 then:	B) if (x > 10):	C) if x > 10:	D) if x > 10 else:
Ans : C) if x>10:

13. Which loop is guaranteed to execute at least once?
A) for	B) while	C) do-while	D) None
Ans : D) none

14. What will def my_func(x, y=5): return x + y return when called with my_func(3)?
A) 3	B) 8	C) Error	D) None
Ans : B) 8

15. What does *args allow you to do in a function?
A) Return multiple values	B) Pass keyword arguments
C) Pass a variable number of positional arguments	D) None of the above
Ans : C) Pass a variable number of positional arduments

16. What is the output of lambda x: x + 10 when called as a function with argument 5?
A) 10	B) 5	C) 15	D) None
Ans : C) 15

17. Which keyword is used to define a class in Python?
A) function	B) define	C) class	D) type
Ans : C) class

18. What is the correct syntax to inherit from a parent class in Python?
A) class Child : Parent		B) class Child inherits Parent:
C) class Child(Parent):		D) class Parent < Child:
Ans : C) class  Child(Parent):

19. Which block is always executed, even if an error occurs in try block?
A) catch	B) raise		C) finally	D) else
Ans :C) finally

20. What mode is used to write a file and overwrite its content?
A) w+	B) r	C) a	D) x
Ans : A) w+ '''






#21.
#A)

'''a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)'''

#B)
'''
x = 10
y = 5

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
'''
m = int(input("Enter marks: "))
if m >= 75:
    print("Distinction")
elif m >= 60:
    print("First Class")
elif m >= 50:
    print("Second Class")
else:
    print("Fail")
'''
#B).
'''
for i in range(1, 101):
    if i % 2 == 0:
        continue
    if i == 89:
        break
    print(i)
'''
#C).
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter number: "))
print(is_prime(num))
'''
#23.A)
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

e1 = Employee("Arun", 2, 50000)
e2 = Employee("Esakki", 3, 60000)
e1.display()
e2.display()
'''
#B).
'''
class Shape:
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

c = Circle(5)
print("Area:", c.area())
print("Radius:", c.get_radius())
'''
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
    print("Program completed.")
'''



















                                 

