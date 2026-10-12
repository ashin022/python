# 1. College Event Registration 
# College Event Registration A college is organizing a technical workshop. A student can register if: ● Their age is between 18 and 25, and ● They are currently a student. Accept the student's age and student status and display whether they are eligible for registration. 
age = int(input("Enter your age:\t "))
is_student = input("Are you currently a student? (yes/no):\t ").strip().lower()
if 18 <= age <= 25 and is_student == "yes":
    print("You are eligible for registration.")
else:
    print("You are not eligible for registration.")



# 2. Online Shopping Discount
# An e-commerce website provides a discount when: ● The order value is ₹3,000 or more, or ● The customer is a premium member. Accept the order amount and membership status. Display whether the customer qualifies for the discount. 
order_amount = int(input("Enter the order amount:\t "))
is_premium_member = input("Are you a premium member? (yes/no):\t ").strip().lower()
if order_amount >= 3000 or is_premium_member == "yes":
    print("You qualify for the discount.")
else:
    print("You do not qualify for the discount.")



# 3. Airport Check-in 
# A passenger can proceed with online check-in if: ● Their ticket is confirmed, ● Their passport is valid, and ● Their departure is more than 2 hours away. Accept the three required values and determine whether online check-in is available. 
ticket_confirmed = input("Is your ticket confirmed? (yes/no):\t ").strip().lower()
passport_valid = input("Is your passport valid? (yes/no):\t ").strip().lower()
departure_time = float(input("Enter the time until departure (in hours):\t "))
if ticket_confirmed == "yes" and passport_valid == "yes" and departure_time > 2:
    print("You can proceed with online check-in.")
else:
    print("You cannot proceed with online check-in.")



# 4. Movie Ticket Booking 
# A cinema offers a special ticket price to customers who are: ● Below 12 years old, or ● 60 years old or above. Accept the customer's age and determine whether they qualify for the special ticket price. 
age = int(input("Enter your age:\t "))
if age < 12 or age >= 60:
    print("You qualify for the special ticket price.")
else:
    print("You do not qualify for the special ticket price.")

# 5. Bank Loan Pre-Eligibility
#A bank wants to perform an initial loan eligibility check. A customer qualifies if: ● Monthly income is at least ₹40,000, ● Credit score is at least 700, and ● The customer does not have an existing loan default. Accept these details and display the eligibility result. 
monthly_income = int(input("Enter your monthly income:\t "))
credit_score = int(input("Enter your credit score:\t "))
existing_loan_default = input("Do you have an existing loan default? (yes/no):\t ").strip().lower()
if monthly_income >= 40000 and credit_score >= 700 and existing_loan_default == "no":
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")



# 6. Food Delivery Free Shipping 
# A food delivery application provides free delivery when: ● The order amount is ₹500 or more, or ● The customer has a premium membership. However, free delivery is not available when the restaurant has temporarily disabled delivery. Accept the required information and determine whether free delivery is available. 
order_amount = int(input("Enter the order amount:\t "))
is_premium_member = input("Are you a premium member? (yes/no):\t").strip().lower()
restaurant_disabled_delivery = input("Has the restaurant temporarily disabled delivery? (yes/no):\t").strip().lower()

if (order_amount >= 500 or is_premium_member == "yes") and restaurant_disabled_delivery == "no":
    print("Free delivery is available.")
else:
    print("Free delivery is not available.")



# 7. Employee Work-from-Home Eligibility 
# An employee can work from home if: ● They have completed at least 6 months in the company, and ● Their current project allows remote work. Accept the employee's experience and project policy and determine whether they can work from home. 
months_completed = int(input("Enter the number of months completed in the company:\t "))
project_allows_remote = input("Does your current project allow remote work? (yes/no):\t").strip().lower()
if months_completed >= 6 and project_allows_remote == "yes":
    print("You can work from home.")
else:
    print("You cannot work from home.")



# 8. Hotel Room Booking 
# A hotel allows a customer to book a room if: ● The room is available, and ● The customer has a valid payment method. However, bookings are not allowed if the hotel has temporarily stopped accepting reservations. Determine whether the booking can proceed. 
room_available = input("Is the room available? (yes/no):\t").strip().lower()
valid_payment_method = input("Do you have a valid payment method? (yes/no):\t").strip().lower()
hotel_accepting_reservations = input("Is the hotel currently accepting reservations? (yes/no):\t").strip().lower()
if room_available == "yes" and valid_payment_method == "yes" and hotel_accepting_reservations == "yes":
    print("You can proceed with the booking.")
else:
    print("You cannot proceed with the booking.")



# 9. Online Exam Access 
# A student can start an online examination if: ● They are logged into their account, ● Their exam registration is confirmed, ● The examination is currently active, and ● Their account is not blocked. Accept these details and determine whether the student can access the exam. 
is_logged_in = input("Are you logged into your account? (yes/no):\t").strip().lower()
exam_registration_confirmed = input("Is your exam registration confirmed? (yes/no):\t").strip().lower()
examination_active = input("Is the examination currently active? (yes/no):\t").strip().lower()
account_not_blocked = input("Is your account not blocked? (yes/no):\t").strip().lower()

if is_logged_in == "yes" and exam_registration_confirmed == "yes" and examination_active == "yes" and account_not_blocked == "yes":
    print("You can access the exam.")
else:
    print("You cannot access the exam.")



# 10. Gym Membership Plan 
# A gym provides a premium membership upgrade if: ● The member has been subscribed for at least 1 year, and ● Their current membership is active. Alternatively, a member can receive the upgrade if they have purchased a yearly plan. Determine whether the member qualifies for the premium upgrade. 
member_subscribed_1_year = input("Have you been subscribed for at least 1 year? (yes/no):\t").strip().lower()
current_membership_active = input("Is your current membership active? (yes/no):\t").strip().lower()
purchased_yearly_plan = input("Have you purchased a yearly plan? (yes/no):\t").strip().lower()

if (member_subscribed_1_year == "yes" and current_membership_active == "yes") or purchased_yearly_plan == "yes":
    print("You qualify for the premium membership upgrade.")
else:
    print("You do not qualify for the premium membership upgrade.")



# 11. Ride Booking Application 
# A customer can book an immediate ride if: ● Their pickup location is within the service area, and ● A driver is currently available. Alternatively, the customer can make a scheduled booking if scheduled rides are enabled. Determine whether the customer can make a booking. 
pickup_within_service_area = input("Is your pickup location within the service area? (yes/no):\t").strip().lower()
driver_available = input("Is a driver currently available? (yes/no):\t").strip().lower()
scheduled_rides_enabled = input("Are scheduled rides enabled? (yes/no):\t").strip().lower()

if pickup_within_service_area == "yes" and driver_available == "yes":
    print("You can book an immediate ride.")
elif scheduled_rides_enabled == "yes":
    print("You can make a scheduled booking.")
else:
    print("You cannot make a booking.")



# 12. E-commerce Product Return 
# An online store accepts a product return if: ● The product was purchased within the last 7 days, ● The product is unused, and ● The product is eligible for return. Determine whether the customer's return request can be accepted.
purchase_within_7_days = input("Was the product purchased within the last 7 days? (yes/no):\t").strip().lower()
product_unused = input("Is the product unused? (yes/no):\t").strip().lower()
product_eligible_for_return = input("Is the product eligible for return? (yes/no):\t").strip().lower()

if purchase_within_7_days == "yes" and product_unused == "yes" and product_eligible_for_return == "yes":
    print("Your return request can be accepted.")
else:
    print("Your return request cannot be accepted.")


# 13. Library Book Borrowing 
# A student can borrow a book from the college library if: ● They have no overdue books, ● Their library membership is active, and ● The requested book is available. Accept the required information and determine whether the student can borrow the book.
no_overdue_books = input("Do you have any overdue books? (yes/no):\t").strip().lower() 
library_membership_active = input("Is your library membership active? (yes/no):\t").strip().lower() 
book_available = input("Is the requested book available? (yes/no):\t").strip().lower() 

if no_overdue_books == "no" and library_membership_active == "yes" and book_available == "yes":
    print("You can borrow the book.")
else:
    print("You cannot borrow the book.")



# 15. Mobile Data Usage Alert 
# A mobile application should display a warning when: ● The user's data usage has reached at least 90% of their monthly limit, or ● Their remaining data is less than 1 GB. However, the warning should not be displayed if the user has an unlimited data plan. Determine whether the warning should be triggered
data_usage_percentage = float(input("Enter your data usage percentage:\t "))
remaining_data_gb = float(input("Enter your remaining data (in GB):\t "))
unlimited_data_plan = input("Do you have an unlimited data plan? (yes/no):\t ").strip().lower() == "yes"
if (data_usage_percentage >= 90 or remaining_data_gb < 1) and not unlimited_data_plan:
    print("Warning: Your data usage is high.")
else:
    print("Your data usage is within limits.")



# 16. Parking Lot Entry 
# A vehicle can enter a parking facility if: ● The vehicle has a valid parking pass, or ● The driver is paying for visitor parking. However, entry is not permitted if the parking lot is full. Determine whether the vehicle can enter. 
parking_pass_valid = input("Does the vehicle have a valid parking pass? (yes/no):\t ").strip().lower() == "yes"
visitor_parking_paid = input("Is the driver paying for visitor parking? (yes/no):\t ").strip().lower() == "yes"
parking_lot_full = input("Is the parking lot full? (yes/no):\t ").strip().lower() == "yes"

if (parking_pass_valid or visitor_parking_paid) and not parking_lot_full:
    print("The vehicle can enter the parking facility.")
else:
    print("The vehicle cannot enter the parking facility.")
# 
# 
#  
# 17. Scholarship Eligibility 
# A student is eligible for a scholarship if: ● Their academic score is at least 85%, and ● Their attendance is at least 75%. Students with an academic score of 95% or higher can qualify regardless of attendance. Determine whether the student is eligible
academic_score = float(input("Enter the student's academic score:\t "))
attendance = float(input("Enter the student's attendance:\t "))

if academic_score >= 95:
    print("The student is eligible for the scholarship.")
elif academic_score >= 85 and attendance >= 75:
    print("The student is eligible for the scholarship.")
else:
    print("The student is not eligible for the scholarship.")



# 18. Food Ordering – Restaurant Availability 
# A customer can place an order if: ● The restaurant is currently open, ● The restaurant delivers to the customer's location, and ● The restaurant is accepting online orders. Determine whether the customer can place an order.
restaurant_open = input("Is the restaurant currently open? (yes/no):\t ").strip().lower() == "yes"
delivers_to_location = input("Does the restaurant deliver to your location? (yes/no):\t ").strip().lower() == "yes"
accepting_online_orders = input("Is the restaurant accepting online orders? (yes/no):\t ").strip().lower() == "yes"

if restaurant_open and delivers_to_location and accepting_online_orders:
    print("The customer can place an order.")
else:
    print("The customer cannot place an order.")



# 19. Smart Home Security 
# A smart home system should activate an alert when: ● Motion is detected, and ● The security system is armed. It should also activate an alert when the main door is opened while the security system is armed. Determine whether the security alert should be triggered. 
motion_detected = input("Is motion detected? (yes/no):\t ").strip().lower() == "yes"
security_system_armed = input("Is the security system armed? (yes/no):\t ").strip().lower() == "yes"
main_door_opened = input("Is the main door opened? (yes/no):\t ").strip().lower() == "yes"

if (motion_detected and security_system_armed) or (main_door_opened and security_system_armed):
    print("The security alert should be triggered.")
else:
    print("The security alert should not be triggered.")


# 20. Travel Insurance Eligibility 
# A person can purchase a particular travel insurance plan if: ● Their age is between 18 and 65, ● Their trip duration is 30 days or less, and ● They are travelling to a country covered by the insurance. However, the plan is unavailable if the destination is currently excluded from coverage. Determine whether the person is eligible for the insurance plan. 
age = int(input("Enter your age:\t "))
trip_duration = int(input("Enter your trip duration (in days):\t "))
destination_covered = input("Is the destination covered by the insurance? (yes/no):\t ").strip().lower() == "yes"
destination_excluded = input("Is the destination currently excluded from coverage? (yes/no):\t ").strip().lower() == "yes"

if 18 <= age <= 65 and trip_duration <= 30 and destination_covered and not destination_excluded:
    print("The person is eligible for the insurance plan.")
else:
    print("The person is not eligible for the insurance plan.")



# 14. Job Application Screening 
# A company is looking for a Python developer. A candidate passes the initial screening if: ● They have at least 1 year of Python experience, and ● They know either Django or FastAPI. Additionally, candidates with 3 or more years of experience are automatically considered for the next stage. Determine whether the candidate qualifies for the next stage
python_experience_years = int(input("Enter your Python experience in years:\t "))
knows_django = input("Do you know Django? (yes/no):\t ").strip().lower() == "yes"
knows_fastapi = input("Do you know FastAPI? (yes/no):\t ").strip().lower() == "yes"

if python_experience_years >= 1 and (knows_django or knows_fastapi):
    if python_experience_years >= 3:
        print("The candidate qualifies for the next stage.")
    else:
        print("The candidate passes the initial screening but does not qualify for the next stage.")
else:
    print("The candidate does not qualify for the next stage.")