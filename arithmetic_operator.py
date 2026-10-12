# # 1.Write a program to add two numbers entered by the user. 
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t "))
# print(n1+n2)

# # 2. Write a program to find the difference between two numbers.
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t "))
# print(n1-n2)

# #3 . Write a program to multiply three numbers. 
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t "))
# n3 = int(input("Enter another number:\t "))
# print(n1*n2*n3)

# # 4. Write a program to divide one number by another
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t ")) 
# print(n1/n2)

# # 5. Write a program to calculate the square of a number.
# n1 = int(input("Enter a number:\t "))
# print(n1**2)

# # 6.Write a program to calculate the cube of a number.
# n1 = int(input("Enter a number:\t "))
# print(n1**3)

# # 7.Write a program to calculate the average of three numbers.
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t "))
# n3 = int(input("Enter another number:\t "))
# print((n1+n2+n3)/3)

# # 8.Write a program to calculate the total price of 5 notebooks if the price of one notebook is entered by the user.
# n1 = int(input("Enter the price of one notebook:\t "))
# print(n1*5)

# # 9. Write a program to find the quotient and remainder when one integer is divided by another. 
# n1 = int(input("Enter a number:\t "))
# n2 = int(input("Enter another number:\t "))
# print("Quotient:", n1//n2)
# print("Remainder:", n1%n2)

# # 10. A shop has 47 chocolates. If each box holds 6 chocolates, calculate: ● The number of completely filled boxes. ● The number of chocolates left over.
# total_chocolates = 47
# chocolates_per_box = 6
# filled_boxes = total_chocolates // chocolates_per_box
# leftover_chocolates = total_chocolates % chocolates_per_box
# print("Number of completely filled boxes:", filled_boxes)
# print("Number of chocolates left over:", leftover_chocolates)

# # 11. Write a program to convert a given number of minutes into complete hours and remaining minutes. 
# total_minutes = int(input("Enter the number of minutes:\t "))
# hours = total_minutes // 60
# remaining_minutes = total_minutes % 60
# print("Complete hours:", hours)
# print("Remaining minutes:", remaining_minutes)

# # 12. Write a program to convert 367 seconds into minutes and remaining seconds.
# total_seconds = 367
# minutes = total_seconds // 60
# remaining_seconds = total_seconds % 60
# print("Minutes:", minutes)
# print("Remaining seconds:", remaining_seconds)

# 13. A teacher wants to distribute 53 students into groups of 8. Calculate the number of complete groups and the students left over. 
total_students = 53
students_per_group = 8
complete_groups = total_students // students_per_group
leftover_students = total_students % students_per_group
print("Number of complete groups:", complete_groups)
print("Number of students left over:", leftover_students)

# 14. Write a program to extract the last digit of a positive integer using the modulus operator.
n = int(input("Enter a positive integer:\t "))
last_digit = n % 10
print("The last digit of", n, "is", last_digit)

# 15. Write a program to remove the last digit of a positive integer using floor division. 
n = int(input("Enter a positive integer:\t "))
n = n // 10
print("The number after removing the last digit is:", n)

# 16. Shopping bill: A customer buys 3 pens costing ₹15 each and 2 notebooks costing ₹40 each. Calculate the total bill. 
pen_cost = 15
notebook_cost = 40
pens_bought = 3
notebooks_bought = 2
total_bill = (pen_cost * pens_bought) + (notebook_cost * notebooks_bought)
print("The total bill is:", total_bill)

# 17. Salary calculation: An employee earns ₹800 per day. Calculate their salary for 26 working days. 
daily_salary = 800
working_days = 26
total_salary = daily_salary * working_days
print("The total salary for", working_days, "working days is:", total_salary)

# 18. Distance conversion: Convert a distance given in kilometers into meters and centimeters.
distance_km = float(input("Enter distance in kilometers:\t "))
distance_meters = distance_km * 1000
distance_centimeters = distance_km * 100000
print("Distance in meters:", distance_meters)
print("Distance in centimeters:", distance_centimeters)

# 19. Rectangle: Accept the length and width of a rectangle and calculate its area and perimeter. 
length = float(input("Enter the length of the rectangle:\t "))
width = float(input("Enter the width of the rectangle:\t "))
area = length * width
perimeter = 2 * (length + width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

# 20. Simple interest: Accept the principal amount, annual interest rate, and time in years. Calculate the simple interest using: SI=(P×R×T) /100 
principal = float(input("Enter the principal amount:\t "))
rate = float(input("Enter the annual interest rate (in %):\t "))
time = float(input("Enter the time in years:\t "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

# 21. Bill sharing: Accept a restaurant bill and the number of friends. Calculate how much each friend should pay if the bill is shared equally. 
bill_amount = float(input("Enter the total restaurant bill:\t "))
number_of_friends = int(input("Enter the number of friends:\t "))
amount_per_friend = bill_amount / number_of_friends
print("Each friend should pay:", amount_per_friend)

# 22. Travel calculation: A car travels 180 km using 12 liters of fuel. Calculate its mileage in km per liter. 
distance_traveled = 180
fuel_used = 12
mileage = distance_traveled / fuel_used
print("The mileage of the car is:", mileage, "km per liter.")

# 23. Unit price: Accept the total price of a packet of rice and its weight in kilograms. Calculate the price per kilogram.
total_price = float(input("Enter the total price of the packet of rice:\t "))
weight_kg = float(input("Enter the weight of the packet in kilograms:\t "))
price_per_kg = total_price / weight_kg
print("The price per kilogram of rice is:", price_per_kg)

# 24. Time conversion: Accept a total number of hours and convert it into complete days and remaining hours.
total_hours = int(input("Enter the total number of hours:\t "))
days = total_hours // 24
remaining_hours = total_hours % 24
print("Complete days:", days)
print("Remaining hours:", remaining_hours)

# 25. Power calculation: Accept a number and an exponent, then calculate the result using the ** operator.
number = float(input("Enter a number:\t "))
exponent = float(input("Enter the exponent:\t "))
result = number ** exponent
print(f"{number} raised to the power of {exponent} is: {result}")