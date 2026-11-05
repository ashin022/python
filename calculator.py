# import module_name 
# module_name.function_name()
# module_name.variable

# import module_name as alias
# alias.function_name()
# alias.variable

# from module_name import *
# function_name1()
# function_name2()
# variable

# from module_name import function_name1, function_name2, variable
# function_name1()
# variable

from mathfunction import add, subtract, multiply, divide,pi
print(pi)
while True:
    choice = input('+ for addition, - for subtraction, * for multiplication, / for division, exit\n enter your choice: ')
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
    except ValueError:
        print("Only integers are allowed..")
        continue
    match choice.strip():
        case '+':
            print(add(n1,n2))
        case '-':
            print(subtract(n1,n2))
        case '*':
            print(multiply(n1,n2))
        case '/':
            print(divide(n1,n2))
        case 'x':
            break
        case _:
            print("Invalid choice")

