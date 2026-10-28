# 1. Student Grade Calculator 
mark = float(input("Enter the student's mark (0-100): "))

if not 0 <= mark <= 100:
	print("Mark must be between 0 and 100.")
elif mark >= 90:
	print("Grade: A+")
elif mark >= 80:
	print("Grade: A")
elif mark >= 70:
	print("Grade: B")
elif mark >= 60:
	print("Grade: C")
elif mark >= 50:
	print("Grade: D")
else:
	print("Grade: Fail")

# 2. ATM Withdrawal System 
balance = float(input("Enter the account balance: ₹"))
amount = float(input("Enter the withdrawal amount: ₹"))

if amount > balance:
	print("Insufficient Balance")
elif amount % 100 != 0:
	print("Enter an amount in multiples of ₹100")
else:
	print("Withdrawal Successful")

# 3. Online Shopping Delivery Charge 
order_value = float(input("Enter the order value: ₹"))

if order_value >= 5000:
	delivery_charge = 0
elif order_value >= 2000:
	delivery_charge = 50
else:
	delivery_charge = 100

final_payable = order_value + delivery_charge
print(f"Delivery charge: ₹{delivery_charge:.2f}")
print(f"Final payable amount: ₹{final_payable:.2f}")


# 4. Employee Performance Rating
score = float(input("Enter the employee's performance score: "))

if score >= 90:
	print("Rating: Excellent")
elif score >= 75:
	print("Rating: Very Good")
elif score >= 60:
	print("Rating: Good")
elif score >= 40:
	print("Rating: Needs Improvement")
else:
	print("Rating: Poor")

# 5. Electricity Bill Calculator 
units = float(input("Enter the units consumed: "))

if units <= 100:
	bill = units * 2
elif units <= 200:
	bill = 100 * 2 + (units - 100) * 3
elif units <= 400:
	bill = 100 * 2 + 100 * 3 + (units - 200) * 5
else:
	bill = 100 * 2 + 100 * 3 + 200 * 5 + (units - 400) * 7

print(f"Total electricity bill: ₹{bill:.2f}")

# 6. Movie Ticket Pricing 
age = int(input("Enter the customer's age: "))

if age < 5:
	ticket_price = 0
elif age <= 12:
	ticket_price = 100
elif age <= 59:
	ticket_price = 200
else:
	ticket_price = 120

print(f"Ticket price: ₹{ticket_price}")

# 7. Traffic Fine System 
speed = float(input("Enter the vehicle speed (km/h): "))

if speed <= 60:
	print("No fine")
elif speed <= 80:
	print("Fine: ₹500")
elif speed <= 100:
	print("Fine: ₹1,000")
else:
	print("Fine: ₹2,000 and License Review")

# 8. Restaurant Billing System
total_bill = float(input("Enter the total bill amount: ₹"))

if total_bill >= 5000:
	discount_rate = 0.20
elif total_bill >= 3000:
	discount_rate = 0.15
elif total_bill >= 1000:
	discount_rate = 0.10
else:
	discount_rate = 0

discount = total_bill * discount_rate
final_bill = total_bill - discount

print(f"Discount: ₹{discount:.2f}")
print(f"Final bill amount: ₹{final_bill:.2f}")

# 9. College Admission Decision 
entrance_score = float(input("Enter the entrance examination score: "))

if entrance_score >= 90:
	print("Direct Admission")
elif entrance_score >= 75:
	print("Admission + Interview")
elif entrance_score >= 60:
	print("Waitlisted")
else:
	print("Not Eligible")

# 10. Bank Loan Risk Category 
credit_score = int(input("Enter the applicant's credit score: "))
has_default = input("Does the applicant have an existing loan default? (yes/no): ").strip().lower()

if has_default == "yes":
	print("Loan Approval Requires Manual Review")
elif credit_score >= 750:
	print("Low Risk")
elif credit_score >= 650:
	print("Medium Risk")
elif credit_score >= 550:
	print("High Risk")
else:
	print("Very High Risk")

# 11. Hotel Room Pricing 
room_type = input("Enter the room type (Standard/Deluxe/Suite): ").strip().lower()
nights = int(input("Enter the number of nights: "))

if room_type == "standard":
	price_per_night = 2000
elif room_type == "deluxe":
	price_per_night = 3500
elif room_type == "suite":
	price_per_night = 5000
else:
	print("Invalid room type")
	price_per_night = 0

total_cost = price_per_night * nights
if nights > 5:
	total_cost *= 0.90

print(f"Final bill: ₹{total_cost:.2f}")


# 12. Employee Bonus Calculator
annual_salary = float(input("Enter the annual salary: ₹"))
performance = float(input("Enter the performance score: "))

if performance >= 90:
	bonus_rate = 0.20
elif performance >= 75:
	bonus_rate = 0.15
elif performance >= 60:
	bonus_rate = 0.10
else:
	bonus_rate = 0

bonus = annual_salary * bonus_rate
print(f"Annual bonus: ₹{bonus:.2f}")

# 13. Mobile Data Plan 
data_usage = float(input("Enter the monthly data requirement (GB): "))

if data_usage < 5:
	plan = "Basic Plan"
	price = 199
elif data_usage <= 20:
	plan = "Standard Plan"
	price = 399
elif data_usage <= 50:
	plan = "Premium Plan"
	price = 699
else:
	plan = "Unlimited Plan"
	price = 999

print(f"Recommended plan: {plan} – ₹{price}/month")

# 14. Parking Fee Calculator
parking_hours = int(input("Enter the parking duration in hours: "))
is_electric = input("Is the vehicle electric? (yes/no): ").strip().lower()

if parking_hours <= 2:
	parking_fee = 30
elif parking_hours <= 5:
	parking_fee = 50
elif parking_hours <= 10:
	parking_fee = 100
else:
	parking_fee = 150

if is_electric == "yes":
	parking_fee *= 0.80

print(f"Final parking fee: ₹{parking_fee:.2f}")

# 15. Online Exam Result 
theory_mark = float(input("Enter the theory mark: "))
practical_mark = float(input("Enter the practical mark: "))

if theory_mark < 40 or practical_mark < 40:
	print("Fail")
else:
	average = (theory_mark + practical_mark) / 2
	if average >= 75:
		print("Distinction")
	elif average >= 60:
		print("First Class")
	elif average >= 50:
		print("Second Class")
	else:
		print("Pass")

# 16. Flight Baggage Fee 
baggage_weight = float(input("Enter the baggage weight (kg): "))
business_class = input("Is the passenger travelling in Business Class? (yes/no): ").strip().lower()

free_limit = 25 if business_class == "yes" else 15

if baggage_weight <= free_limit:
	baggage_charge = 0
elif baggage_weight <= 20:
	baggage_charge = 500
elif baggage_weight <= 30:
	baggage_charge = 1000
else:
	baggage_charge = 2000

print(f"Baggage charge: ₹{baggage_charge}")

# 17. E-Commerce Return Eligibility 
days_since_purchase = int(input("How many days ago was the product purchased? "))
is_unused = input("Is the product unused? (yes/no): ").strip().lower() == "yes"
is_returnable = input("Is the product returnable? (yes/no): ").strip().lower() == "yes"

if days_since_purchase > 7:
	print("Return Rejected: The product was purchased more than 7 days ago.")
elif not is_unused:
	print("Return Rejected: The product has been used.")
elif not is_returnable:
	print("Return Rejected: This product is not returnable.")
else:
	print("Return Approved")

# 18. Salary Tax Calculator 
annual_salary = float(input("Enter your annual salary: ₹"))

if annual_salary <= 300000:
	tax_rate = 0
elif annual_salary <= 600000:
	tax_rate = 0.05
elif annual_salary <= 1000000:
	tax_rate = 0.10
else:
	tax_rate = 0.20

tax_amount = annual_salary * tax_rate
final_salary = annual_salary - tax_amount

print(f"Tax amount: ₹{tax_amount:.2f}")
print(f"Final salary after tax: ₹{final_salary:.2f}")

# 19. Ride Fare Calculator 
distance = float(input("Enter the ride distance in km: "))
is_peak_hour = input("Is the ride during peak hours? (yes/no): ").strip().lower() == "yes"

if distance <= 5:
	fare = 100
elif distance <= 15:
	fare = 100 + (distance - 5) * 15
elif distance <= 30:
	fare = 100 + (10 * 15) + (distance - 15) * 12
else:
	fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

if is_peak_hour:
	fare *= 1.20

print(f"Final ride fare: ₹{fare:.2f}")

# 20. Employee Leave Approval System
available_leave = int(input("Enter available leave days: "))
requested_leave = int(input("Enter requested leave days: "))

if requested_leave > available_leave:
	decision = "Leave Rejected"
elif requested_leave <= 3:
	decision = "Leave Automatically Approved"
elif requested_leave <= 7:
	decision = "Manager Approval Required"
else:
	decision = "HR Approval Required"

print(decision)