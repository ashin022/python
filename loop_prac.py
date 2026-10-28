# For Loop

# 1.Print numbers from 1 to 10 using a for loop.
for number in range(1, 11):
	print(number)

# 2.Print the multiplication table of a given number.
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
	print(f"{number} x {multiplier} = {number * multiplier}")

# 3.Find the sum of all numbers from 1 to n.
n = int(input("Enter a number n: "))
total = 0
for number in range(1, n + 1):
	total += number
print(f"The sum of all numbers from 1 to {n} is {total}")

# 4.Print the first n Fibonacci numbers.
n = int(input("Enter the number of Fibonacci numbers: "))
first, second = 0, 1
for _ in range(n):
	print(first)
	first, second = second, first + second
	
# 5. Print a pattern like:
#    *
#    **
#    *
#    **
for stars in (1, 2, 1, 2):
	print("*" * stars)

# 6.Reverse a string using a loop.
text = input("Enter a string: ")
reversed_text = ""
for character in text:
	reversed_text = character + reversed_text
print(f"Reversed string: {reversed_text}")

# 7.Reverse a string using a loop.
text = input("Enter a string: ")
reversed_text = ""
for character in text:
	reversed_text = character + reversed_text
print(f"Reversed string: {reversed_text}")

# While Loop Questions

# 8.Print numbers from n to 1 using a while loop.
n = int(input("Enter a number n: "))
while n >= 1:
	print(n)
	n -= 1

# 9.Find the factorial of a number using a while loop.
n = int(input("Enter a non-negative number: "))
factorial = 1
while n > 1:
	factorial *= n
	n -= 1
print(f"Factorial: {factorial}")

# 10.Print all digits of a number separately.
number = int(input("Enter a number: "))
for digit in str(abs(number)):
	print(digit)

# 11.Count the number of digits in a given number.
number = abs(int(input("Enter a number: ")))
digit_count = 0
if number == 0:
	digit_count = 1
else:
	while number > 0:
		digit_count += 1
		number //= 10
print(f"Number of digits: {digit_count}")

# 12.Keep taking user input until they enter "exit".
while True:
	user_input = input("Enter text (or 'exit' to quit): ")
	if user_input == "exit":
		break

# Loop Control Statements
	
# 13.Use break to stop the loop when a number is found in a list.
numbers = [3, 7, 12, 18, 24]
target = int(input("Enter a number to find: "))
for number in numbers:
	if number == target:
		print(f"Found {target} in the list")
		break
else:
	print(f"{target} was not found in the list")

# 14.Use continue to skip printing even numbers from 1 to 20.
for number in range(1, 21):
	if number % 2 == 0:
		continue
	print(number)

# 15.Use pass inside a loop without affecting its flow.
for number in range(1, 4):
	pass
	print(number)

# Match Statements
# 1.Day classifier: Take a number 1-7 and print the weekday. Use case 6|7 for weekend.
day = int(input("Enter a number from 1 to 7: "))
match day:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6 | 7:
		print("Weekend")
	case _:
		print("Invalid day")

# 2.Simple calculator: choose an operation using match.
a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter an operation (+, -, *, /): ")
match op:
	case "+":
		print(a + b)
	case "-":
		print(a - b)
	case "*":
		print(a * b)
	case "/":
		if b == 0:
			print("Cannot divide by zero")
		else:
			print(a / b)
	case _:
		print("Invalid operation")

# 3. Grade checker: classify marks from 0 to 100.
marks = int(input("Enter marks (0-100): "))
match marks:
	case score if 90 <= score <= 100:
		print("A")
	case score if 80 <= score < 90:
		print("B")
	case score if 70 <= score < 80:
		print("C")
	case score if 60 <= score < 70:
		print("D")
	case score if 0 <= score < 60:
		print("F")
	case _:
		print("Invalid marks")

# 4. HTTP status handler.
status = int(input("Enter an HTTP status code: "))
match status:
	case 200:
		print("OK")
	case 404:
		print("Not Found")
	case code if 500 <= code <= 599:
		print("Server Error")
	case code if code >= 400:
		print("Client Error")

# 5. Determine the color of a chessboard square.
row = int(input("Enter the row: "))
col = int(input("Enter the column: "))
match (row % 2, col % 2):
	case (0, 0) | (1, 1):
		print("Black")
	case _:
		print("White")

# 6. Command parser.
import ast

cmd = ast.literal_eval(input('Enter a command (for example, ["add", 5, 3] or ["quit"]): '))
match cmd:
	case ["add", a, b]:
		print(a + b)
	case ["quit"]:
		print("Goodbye")
	case _:
		print("Invalid command")

# 7. File type checker.
filename = input('Enter a filename (for example, "photo.jpg"): ')
parts = filename.split(".")
match parts:
	case [name, "jpg" | "png"]:
		print("Image")
	case [name, "py"]:
		print("Python file")
	case _:
		print("Unknown file type")

# 8. Shape area calculator.
shape = ast.literal_eval(input('Enter a shape (for example, ("circle", 5) or ("rect", 4, 3)): '))
match shape:
	case ("circle", radius):
		print(3.141592653589793 * radius ** 2)
	case ("rect", length, width):
		print(length * width)
	case _:
		print("Invalid shape")