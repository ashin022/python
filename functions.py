# function is a block of code that is designed to perform a specific task. It can take inputs, process them, and return an output. Functions help in organizing code, making it reusable, and improving readability. In Python, functions are defined using the `def` keyword followed by the function name and parentheses.

# def function_name(parameter1):
#     # code block
#     pass  # placeholder for future code
#     return 'result'

# function_name(arguments)

# def greet():
#    print("fhello")
#    greet()  # calling the function
   
   
# def greet(user):
#     print(f"hello, {user}!!")
    

# greet("Amal")  # calling the function with an argument

# def greet(user):
#     return f"hello, {user}!!"

# result = greet("Amal")
# print(result)  # calling the function and printing the returned value


# def greet(msg,user="Guest"):
#     return f"hello, {user}!! {msg}...."

# result1 = greet("Good morning", "Amal")
# result2 = greet("Good morning")  # using default value for user

# print(result1)
# print(result2)


# def add(a,*args):
#     sum = 0
#     for n in args:
#         sum+=n
#     print(f"Sum is: {sum}")
    
#     add("hello", 1,2,3,4,5)  # calling the function with variable number of arguments
#     add("hello", 10,20,30)  # calling the function with variable number of arguments
#     add("hello", 100,200,300,400,500)  # calling the function with variable number of arguments
#     add("hello", 1,2,3,4,5)  # calling the function with variable number of arguments
    

# print(1)
# print(1,2)
# print(1,2,3)
# print(1,2,3,4)

# def greet(msg,user):
#     return f"hello, {user}!! {msg}...."

# print(greet(user="Amal", msg="Good morning"))  # calling the function with keyword arguments

# def greet(msg,**kwargs):
#     print(kwargs)

# greet(user="Amal", msg="Good morning")  # calling the function with keyword arguments


# def add(a,b):
#     return a+b

# def multiply(a,b):
#     return a*b

# def subtract(a,b):
#     return a-b

# def divide(a,b):
#     return a/b

# while True:
#     choice = input('+ for addition, - for subtraction, * for multiplication, / for division, exit\n enter your choice: ')
#     try:
#         n1 = int(input("Enter first number: "))
#         n2 = int(input("Enter second number: "))
#     except ValueError:
#         print("Only integers are allowed..")
#         continue
#     match choice.strip():
#         case '+':
#             print(add(n1,n2))
#         case '-':
#             print(subtract(n1,n2))
#         case '*':
#             print(multiply(n1,n2))
#         case '/':
#             print(divide(n1,n2))
#         case 'x':
#             break
#         case _:
#             print("Invalid choice")
            
            


# lambda parameters: statement          

# n = 5
# def square(x):
#     return x *x
# print(square(n))
# print(square(10))
# print(square(20))
# print(square(30))

# square = lambda x: x*x
# print(square(4))
# print(square(10))
# print(square(20))
# print(square(30))

# def type_of_number(n):
#     if n > 0:
#         return "Positive"
#     elif n < 0:
#         return "Negative"
#     else:
#         return "Zero"


# trueexpression if condition else falseexpression

# check_type = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

# print(check_type(5))
# print(check_type(-5))
# print(check_type(0))


from functools import reduce

l1 = [10,22,62,111,222,67]
squared_numbers = list(map(lambda x: x*x, l1))
even_numbers = filter(lambda x: x%2==0, l1)
result = reduce(lambda x,y: x+y, l1)
print(squared_numbers)
print(list(even_numbers))
print(result)
