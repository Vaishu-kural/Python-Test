#21
#(A)Accept two numbers
'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Modulus (%):", a % b)
print("Floor Division (//):", a // b)
print("Exponent (**):", a ** b)'''

#(B) All Other Operators
'''
x = 10
y = 20

# Assignment
x += 5
print("After x += 5:", x)

# Comparison
print("x > y:", x > y)
print("x == y:", x == y)

# Logical
print("Logical AND:", (x < y) and (y > 5))

# Identity
print("Identity is:", x is y)
print("Identity is not:", x is not y)

# Membership
lst = [10, 20, 30]
print("20 in list:", 20 in lst)
print("40 not in list:", 40 not in lst)'''

#(c) List Operations
'''
# Initialize list
items = [12, 5, 7, 22, 9]

# Insert
items.insert(2, 99)

# Delete
items.remove(22)

# Update
items[1] = 55

# Sort
items.sort()

# Reverse
items.reverse()

print("Final List:", items)

# Loop through list
for item in items:
    print(item)'''

#22
#(a) Conditional Statements
'''
marks = int(input("Enter marks: "))

if marks > 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")'''

#(b) Loops with Flow Control
'''
for i in range(1, 101):
    
    if i % 2 == 0:
        continue  

    if i == 73:
        break     

    if i == -1:
        pass      

    print(i)'''

#(C)
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("Prime?" , is_prime(num))
'''

#23
#(a) Class and Object
'''
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


# Create objects
e1 = Employee("manno", 101, 50000)
e2 = Employee("arun", 102, 60000)

e1.display()
e2.display()'''

#(b) Inheritance Example
'''
class Shape:
    def area(self):
        return "Area not defined"


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius   # Encapsulated attribute

    # Getter
    def get_radius(self):
        return self.__radius

    # Setter
    def set_radius(self, r):
        if r > 0:
            self.__radius = r

    # Method overriding
    def area(self):
        return 3.14 * self.__radius ** 2


c = Circle(5)
print("Radius:", c.get_radius())
print("Area:", c.area())
c.set_radius(7)
print("Updated Radius:", c.get_radius())
print("Updated Area:", c.area())
'''

#(c) Exception Handling

'''
try:
    n = int(input("Enter a number: "))
    print("Result:", 100 / n)

except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    print("Program ended. Thank you!")

'''




