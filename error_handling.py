# 1. NameError - variable not defined
# print(x)

# 2. TypeError - Invalid type used in operation
# print(1+'1')

# 3. ValueError - Wrong value
# n = int('1f')

# 4. IndexError - Index out of range
# l1 = [1,2]
# print(l1[2])

# 5. KeyError - Dictionary key missing
# student = {"name":"Amal"}
# print(student['rno'])

# 6. AttributeError
# print('hello'.pop(5))

# 7. ZeroDivisionError
# print(10/0)

# 8. FileNotFoundError
# 9. ModuleNotFoundError

# Exception handling
# Syntax:
# try:
#     Code that may generate error
# except ExceptionClass:
#     error handling code
# else:
#     executes if no errors occured
# finally:
#     executes in any case

try:
    n = int(input("Enter a number: "))
    result = 56/n
except ValueError:
    print("Only integers are allowed..")
# except ZeroDivisionError:
#     print("Zero is not allowed")
# except (ValueError, ZeroDivisionError):
#     print("non-integers and zeros are not allowed")
except Exception as e:
    print("Error occured")
else:
    print(result)
finally:
    print("Exception completed")

print("After try-except block")