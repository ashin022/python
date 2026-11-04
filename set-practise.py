# 1. Students Enrolled in Courses 
python_students = {"Arun", "Megha", "Rahul", "Sneha"}
analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}

both_courses = python_students & analytics_students
only_python = python_students - analytics_students
only_analytics = analytics_students - python_students
all_students = python_students | analytics_students
exactly_one_course = python_students ^ analytics_students

print("Students enrolled in both courses:", both_courses)
print("Students enrolled only in Python:", only_python)
print("Students enrolled only in Data Analytics:", only_analytics)
print("All unique students:", all_students)
print("Students enrolled in exactly one course:", exactly_one_course)


# 2. Mobile Brands Purchased by Customers
customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}

common_brands = customer1 & customer2
all_brands = customer1 | customer2
only_customer1 = customer1 - customer2
one_customer_only = customer1 ^ customer2

print("Brands purchased by both customers:", common_brands)
print("All brands purchased:", all_brands)
print("Brands purchased only by customer 1:", only_customer1)
print("Brands purchased by only one customer:", one_customer_only)


# 3. Employees Using Software Tools
design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

common_tools = design_team & marketing_team
design_only = design_team - marketing_team
all_tools = design_team | marketing_team
one_team_only = design_team ^ marketing_team

print("Tools used by both teams:", common_tools)
print("Tools exclusive to the design team:", design_only)
print("All software tools used in the company:", all_tools)
print("Tools used by only one team:", one_team_only)


# 4. Cricket and Football Fans
cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
football_fans = {"Nisha", "Rahul", "Ajay", "David"}

both_sports = cricket_fans & football_fans
only_cricket = cricket_fans - football_fans
only_football = football_fans - cricket_fans
all_sports_fans = cricket_fans | football_fans

print("Students who like both sports:", both_sports)
print("Students who like only cricket:", only_cricket)
print("Students who like only football:", only_football)
print("All sports fans:", all_sports_fans)


# 5. Online Shopping Categories
electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

common_products = electronics & accessories
electronics_only = electronics - accessories
all_purchased_items = electronics | accessories
one_category_only = electronics ^ accessories

print("Products purchased from both categories:", common_products)
print("Products only in electronics:", electronics_only)
print("All purchased items:", all_purchased_items)
print("Products available in only one category:", one_category_only)


# 6. Languages Known by Employees
employee1 = {"Python", "Java", "SQL", "C"}
employee2 = {"Python", "JavaScript", "SQL", "Go"}

common_languages = employee1 & employee2
employee1_only = employee1 - employee2
all_languages = employee1 | employee2
one_employee_only = employee1 ^ employee2

print("Programming languages known by both employees:", common_languages)
print("Languages known only by employee 1:", employee1_only)
print("All unique programming languages:", all_languages)
print("Languages known by only one employee:", one_employee_only)


# 7. OTT Platform Subscriptions
friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}

common_subscriptions = friend1 & friend2
friend1_only = friend1 - friend2
all_ott_platforms = friend1 | friend2
one_friend_only = friend1 ^ friend2

print("OTT platforms subscribed to by both friends:", common_subscriptions)
print("OTT platforms subscribed to only by friend 1:", friend1_only)
print("All OTT platforms:", all_ott_platforms)
print("OTT platforms subscribed to by only one friend:", one_friend_only)


# 8. Available and Sold Products
available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
sold_products = {"Mouse", "Monitor"}

remaining_products = available_products - sold_products
print("Remaining available products:", remaining_products)
print("Sold products:", sold_products)

available_products.add("Printer")
available_products.remove("Keyboard")
print("Available products after adding Printer and removing Keyboard:", available_products)


# 9. College Event Participation
music_event = {"Anu", "David", "Riya", "Sam"}
dance_event = {"Riya", "Sam", "Karthik", "John"}

both_events = music_event & dance_event
music_only = music_event - dance_event
dance_only = dance_event - music_event
all_participants = music_event | dance_event

print("Students participating in both events:", both_events)
print("Students participating only in music:", music_only)
print("Students participating only in dance:", dance_only)
print("All event participants:", all_participants)


# 10. Website Visitors
campaign_A = {"user101", "user102", "user103", "user104"}
campaign_B = {"user103", "user104", "user105", "user106"}

common_visitors = campaign_A & campaign_B
campaign_A_only = campaign_A - campaign_B
total_unique_visitors = campaign_A | campaign_B
one_campaign_only = campaign_A ^ campaign_B

print("Visitors from both campaigns:", common_visitors)
print("Visitors unique to campaign A:", campaign_A_only)
print("Total unique visitors:", total_unique_visitors)
print("Visitors from only one campaign:", one_campaign_only)


# 11. Food Delivery App
restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}

common_food_items = restaurant1 & restaurant2
restaurant1_only = restaurant1 - restaurant2
restaurant2_only = restaurant2 - restaurant1
all_food_items = restaurant1 | restaurant2
one_restaurant_only = restaurant1 ^ restaurant2

print("Food items available at both restaurants:", common_food_items)
print("Food items exclusive to restaurant 1:", restaurant1_only)
print("Food items exclusive to restaurant 2:", restaurant2_only)
print("All available food items:", all_food_items)
print("Food items available at only one restaurant:", one_restaurant_only)