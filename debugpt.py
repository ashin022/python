# Level 1 — Variables & Data Types 
# 1.
name = "Rahul" 
age = "20" 
print("Name:", name) 
print("Age next year:", int(age) + 1) 

# 2.
student_name = "Anu"
student_age = 21
student_course = "Python"
print(student_name)
print(student_age)
print(student_course)

# 3.
price = 99.50
quantity = "3"
total = price * int(quantity)
print("Total:", total)

#4.
x = 10
y = 20
total = x + y
print(total) 

# 5.
first_name = "Arun"
last_name = "Kumar"
full_name = first_name + " " + last_name
print("Full name: " + full_name)
print("Name length:", len(full_name))

# Level 2 — Operators 
# 6.
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a // b)
print("Remainder:", a % b)

# 7.
marks = 75
if marks == 75:
    print("Marks are 75")

# 8.
age = 20
if age > 18 and age < 25:
    print("Eligible")

# 9.
a = 10
b = 20
result = a > b or a < b
print("Result:", result) 

# 10.
x = 10
y = 3
print(x * y)
print(x ^ y)

# Level 3 — Input & Type Conversion 
# 11.
age = int(input("Enter your age: ")) 
if age >= 18: 
    print("Adult") 
else: 
    print("Minor")

# 12.
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
sum = num1 + num2 
print("Sum:", sum) 
# 13.
temperature = float(input("Enter temperature: ")) 
if temperature > 30: 
    print("Hot") 
else: 
    print("Normal") 

# 14.
radius = float(input("Enter radius: ")) 
area = 3.14 * radius * radius 
print("Area:", area) 

# Level 4 — Conditional Statements 
# 15. 
marks = 85
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# 16.
age = 17
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# 17.
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 18.
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Level 5 — if, elif, else 

# 19.
marks = 65
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(grade)

# 20.
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 21.
age = 25
if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")

# Level 6 — Combined Debugging 

# 22.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(name + " is eligible to vote")
else:
    print(name + " is not eligible to vote")

# 23.
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Final price:", final_price)

# 24.
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Invalid")

# 25.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")

# Level 7 — Challenge Questions 

# 26.
year = int(input("Enter your birth year: "))
age = 2026 - year
print("Your age is:", age)

# 27.
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# 28.
marks = 82
attendance = 78
if marks >= 50 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible")

# 29.
a = 10
b = 20
c = 30
if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

print("Largest:", largest)

# 30. Final Challenge
username = input("Enter username: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if username == "student" and age >= 18:
    if marks >= 50:
        print("Admission successful")
    elif marks >= 40:
        print("Admission pending")
    else:
        print("Admission rejected")
else:
    print("Admission rejected")

# Python Debugging — Set 2: Collections

# 1. Lists — Adding Elements
students = ["Anu", "Rahul", "Meera"]
students.append("Arun")
print(students)

# 2. Lists — Indexing
marks = [78, 85, 92, 67, 88]
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# 3. Lists — Updating Elements
fruits = ["Apple", "Banana", "Orange"]
fruits[2] = "Mango"
print(fruits)

# 4. Lists — Removing Elements
subjects = ["Python", "Java", "HTML", "CSS"]
subjects.remove("Java")
print(subjects)

# 5. Lists — Sorting
numbers = [45, 12, 78, 23, 9]
numbers.sort()
print(numbers)

# 6. Tuples — Updating Elements
student = ("Rahul", 21, "Python")
student = (student[0], 22, student[2])
print(student)

# 7. Tuple Unpacking
student = ("Anu", 21, "Data Science")
# The tuple has three values, so unpacking into two variables raises a ValueError.
name, age, subject = student
print(name)
print(age)

# 8. Sets — Adding Elements
numbers = {10, 20, 30, 40}
numbers.add(50)
print(numbers)

# 9. Sets — Duplicate Values
# Sets keep only unique values, so duplicate entries are discarded.
# Use a list to count every entered value, including duplicates.
numbers = [10, 20, 20, 30, 30, 30]
print(len(numbers))  # 6

# 10. Dictionaries — Safely Accessing a Key
student = {
    "name": "Arun",
    "age": 20,
    "course": "Python"
}
if "marks" in student:
    print(student["marks"])
else:
    print("Marks not available")

# 11. Dictionary — Updating
student = {"name": "Meera", "age": 21}
student["age"] = 22  # Use = to assign; == only compares values.
print(student)

# 12. Dictionary — Adding Data
student = {"name": "Rahul", "course": "Python"}
student["age"] = 20
print(student)

# Part B — Functions
# 13. Function Definition
def greet():
    print("Hello, students!")

greet()

# 14. Function Call
def welcome():
    print("Welcome to Python")

welcome()

# 15. Parameters
def greet(name):
    print("Hello", name)

greet("students")

# Part B — Functions (continued)
# 16. Multiple Parameters
def add(a, b):
    print("Sum:", a + b)

add(10, 5)

# 17. Return Value
def square(number):
    return number * number

result = square(5)
print(result)

# 18. return vs print
def add(a, b):
    print("Calculation completed")
    return a + b

result = add(10, 20)
print(result)

# 19. Local Variable
def calculate():
    total = 100
    return total

total = calculate()
print(total)

# 20. Default Arguments
def greet(name, message="Good morning", additional_message=""):
    print(message, name)
    if additional_message:
        print(additional_message)

greet("Anu", "Good evening", "Welcome")

# 21. Function Logic
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = is_even(10)
print(result)

# 22. Function with Input
def calculate_area():
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    return area

print(calculate_area())

# Part C — Modules
# 23. Importing a Module
import math

print(math.sqrt(25))

# 24. Using Module Functions
import math

number = 16
print(math.sqrt(number))

# 25. Import Specific Function
from math import sqrt

print(sqrt(49))

# 26. Random Module
import random

number = random.randint(1, 100)
print("Random number:", number)

# 27. Module Alias
import math as m

print(m.pi)

# 28. Date and Time
from datetime import date

today = date.today()
print(today)

# Part D — Combined Challenges
# 29. Collection + Function
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

marks = [75, 80, 90, 85]
print("Average:", calculate_average(marks))

# 30. Function + Dictionary
def display_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student.get("course", "Not available"))

student = {"name": "Arun", "age": 21}
display_student(student)

# 31. Function + Set
def count_unique(numbers):
    return len(set(numbers))

numbers = [10, 20, 10, 30, 20, 40]
print("Unique numbers:", count_unique(numbers))

# 32. Module + Function
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

print(calculate_circle_area(5))

# 33. List + Function + Conditional
def find_passed_students(marks):
    passed = []
    for mark in marks:
        if mark >= 40:
            passed.append(mark)
    return passed

marks = [35, 40, 45, 60, 72]
print(find_passed_students(marks))

# 34. Dictionary + Function + Module
import math

def calculate_discount(price, percentage):
    discount = price * percentage / 100
    return price - discount

product = {"name": "Laptop", "price": 50000, "discount": 10}
final_price = calculate_discount(product["price"], product["discount"])
print("Final price:", math.floor(final_price))

# 35. Final Challenge
import random

def generate_student():
    student = {
        "name": "Rahul",
        "marks": [78, 85, 92, 67]
    }

    average = sum(student["marks"]) / len(student["marks"])
    student["average"] = average

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    student["grade"] = grade
    student["id"] = random.randint(1000, 9999)
    return student

result = generate_student()
print("Student:", result["name"])
print("Average:", result["average"])
print("Grade:", result["grade"])
print("ID:", result["id"])