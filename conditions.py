# control statements .......

#descision making statements
#loop statements
#loop control statements


# if statement
# if condition:

# body of if 

#       .
#       .
#       .

# if-else statement
# if condition:

#    body of if

#    .
#    .

# else:

#  body of else

age = 20
 
 # if age >= 18:
 #  print('adult')
 
# if age >= 18:
#      print('adult')
# else:
#      print('child')
     
# print("end of if")

# amount = int(input("Enter the total amount:\t "))
# if amount >= 5000:
#     print("free delivery avilable")
# else:
# amount += 40
# print("free delivery not avilable)
# print("total payable :",amount)


# if elif-else statement

#if condition1:
#     body
#elif condition2:
#     body
#elif condition3:
#     .
#     .
#     .
#else:

#   block of else 


# mark = int(input("Enter the mark:\t "))
# if mark >= 90:
#     print("A grade")
# elif mark >= 80:
#     print("B grade")
# elif mark >= 70:
#     print("C grade")
# elif mark >= 60:
#     print("D grade")
# elif mark >= 50:
#     print("E grade")
# elif mark >= 40:
#     print("F grade")
# else:
#     print("invalid mark entry")    
    
    
    
    
# age = 19 

# if age >= 18:
#     print("passed age requirements.")
#     mark = 40
#     if mark > 50 :
#         print("admission granted")
#     else:
#         print("admission denied: insufficient marks")
# else:
#     print("admission denied: under age")   
    
    

# day = input('enter the number of day:') 
# match day:
#     case '1':
#         print('monday')
#     case '2':
#         print('tuesday')
#     case '3':
#         print('wednesday')
#     case '4':
#         print('thursday')
#     case '5':
#         print('friday')
#     case '6':
#         print('saturday')
#     case '7':
#         print('sunday')
#     case _:
#         print('invalid day')
        

age = int(input("Enter your age:\t"))
# match age>= 18:
#     case True:
#         print("adult")
#     case False:
#         print("child")

# day = input("Enter the day:\t")
# match day:
#     case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
#         print("weekday")
#     case "saturday" | "sunday":
#         print("weekend")
#     case _:
#         print("invalid day")

result = "adult" if age >= 18 else "child"
print(result)

# trueexpression if condition else falseexpression

n = 56
even_or_odd = "even" if n % 2 == 0 else "odd"
print(even_or_odd)

