# Basic If-Else Questions

# 1.Write a program that checks if a number is positive, negative, or zero.
number = float(input("Enter a number: "))

if number > 0:
	print("The number is positive.")
elif number < 0:
	print("The number is negative.")
else:
	print("The number is zero.")

# 2.Check if a given number is even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
	print("The number is even.")
else:
	print("The number is odd.")

# 3.Determine if a user is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if age >= 18:
	print("You are eligible to vote.")
else:
	print("You are not eligible to vote.")

# 4.Write a program that takes a temperature input and prints "Cold" if it's below 20°C, "Warm" if between 20-30°C, and "Hot" if above 30°C
temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
	print("Cold")
elif temperature <= 30:
	print("Warm")
else:
	print("Hot")

# 5.Check if a given year is a leap year.
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
	print("The year is a leap year.")
else:
	print("The year is not a leap year.")


# Nested If Questions

# 6. Take input for marks and print grades as per the following:
#    - 90+ → A
#    - 80-89 → B
#    - 70-79 → C
#    - 60-69 → D
#    - Below 60 → F
marks = float(input("Enter your marks: "))

if marks >= 90:
	print("Grade: A")
elif marks >= 80:
	print("Grade: B")
elif marks >= 70:
	print("Grade: C")
elif marks >= 60:
	print("Grade: D")
else:
	print("Grade: F")

#7. Write a program to check if a number is positive and even; otherwise, print "Not positive or not even."
number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
	print("The number is positive and even.")
else:
	print("Not positive or not even.")

# 8.Given three numbers, find the largest number among them.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
	print("The largest number is:", number1)
elif number2 >= number1 and number2 >= number3:
	print("The largest number is:", number2)
else:
	print("The largest number is:", number3)


# If-Elif-Else Questions

# 9. A shop gives discounts based on purchase amount:
#    - Above ₹5000 → 20% discount
#    - ₹2000-₹5000 → 10% discount
#    - Below ₹2000 → No discount
#    Write a program to calculate the final bill amount.
purchase_amount = float(input("Enter the purchase amount: ₹"))

if purchase_amount > 5000:
	discount = 0.20
elif purchase_amount >= 2000:
	discount = 0.10
else:
	discount = 0

final_bill = purchase_amount * (1 - discount)
print("Final bill amount: ₹", final_bill)

# 10.Convert a numerical day (1-7) into its corresponding weekday name (1 → Monday, 2 → Tuesday, etc.).
day = int(input("Enter a day number (1-7): "))

if day == 1:
	print("Monday")
elif day == 2:
	print("Tuesday")
elif day == 3:
	print("Wednesday")
elif day == 4:
	print("Thursday")
elif day == 5:
	print("Friday")
elif day == 6:
	print("Saturday")
elif day == 7:
	print("Sunday")
else:
	print("Invalid day number. Please enter a number from 1 to 7.")