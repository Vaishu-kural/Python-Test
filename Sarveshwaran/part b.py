# #21a)
# # Accept two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Arithmetic Operations Results:")
# print("Addition (+):", a + b)
# print("Subtraction (-):", a - b)
# print("Multiplication (*):", a * b)

# # Avoid division by zero
# if b != 0:
#     print("Division (/):", a / b)
#     print("Modulus (%):", a % b)
#     print("Floor Division (//):", a // b)
# else:
#     print("Division, Modulus, Floor Division not possible (b = 0)")

# print("Exponent (**):", a ** b)

# # Assignment Operators
# x = 10
# print("Initial value:", x)

# x += 5
# print("x += 5:", x)

# x -= 3
# print("x -= 3:", x)

# x *= 2
# print("x *= 2:", x)

# # 21b
# # Comparison Operators
# a = 10
# b = 20

# print("a == b:", a == b)
# print("a != b:", a != b)
# print("a > b:", a > b)
# print("a < b:", a < b)

# # Logical Operators
# print("Logical AND:", a < b and b > 15)
# print("Logical OR:", a > b or b > 15)
# print("Logical NOT:", not(a > b))

# # 21 c 
# # Identity Operators
# list1 = [1, 2, 3]
# list2 = list1
# list3 = [1, 2, 3]

# print("list1 is list2:", list1 is list2)
# print("list1 is list3:", list1 is list3)

# # Membership Operators
# nums = [10, 20, 30, 40]

# print("20 in nums:", 20 in nums)
# print("50 not in nums:", 50 not in nums)



# #22 a)
# marks = int(input("Enter your marks: "))

# if marks > 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First class")
# elif marks >= 50:
#     print("Second class")
# else:
#     print("Fail")

# # #22. b)
# for i in range(1, 101):
    
#     if i == 73:
#         break   # stop at 73
    
#     if i % 2 == 0:
#         continue   # skip even numbers
    
#     pass   # placeholder (no operation)
    
#     print(i)


# # #22c) 
# def is_prime(num):
#     if num <= 1:
#         return False
    
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
    
#     return True

# # Function call
# n = int(input("Enter a number: "))

# if is_prime(n):
#     print("True (Prime Number)")
# else:
#     print("False (Not a Prime Number)")

 #23. a) 
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("------------------------")


# Creating objects
emp1 = Employee("Sarvesh", 101, 50000)
emp2 = Employee("Arun", 102, 60000)

# Displaying details
emp1.display()
emp2.display()

#23b 
class Shape:
    def area(self):
        print("This is a shape")


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius   # Encapsulation (private variable)

    # Getter
    def get_radius(self):
        return self.__radius

    # Setter
    def set_radius(self, r):
        self.__radius = r

    # Method overriding
    def area(self):
        print("Area of Circle:", 3.14 * self.__radius * self.__radius)


# Object creation
c = Circle(5)

# Using getter
print("Radius:", c.get_radius())

# Using overridden method
c.area()

# Using setter
c.set_radius(10)
print("Updated Radius:", c.get_radius())
c.area()


#23. c) 
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    print("Execution completed.")