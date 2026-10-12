# Arithmetic Operators
a = 10
b = 5

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b ) # Floor Division


# assignment Operators
# -(assign)
a+= 5
a-=5
a*=5
a/=5
a%=5
a**=5
a//=5

print(a)


#comparison Operators
print(a < b) # less than
print(a > b) # greater than
print(a <= b) # less than or equal to
print(a >= b) # greater than or equal to
print(a == b) # equal to
print(a != b) # not equal to


#logical Operators

# AND
# OR

age = 25
has_voter_id = True
eligible_for_vote = age >= 18 and has_voter_id
print(eligible_for_vote) # True


#condition1         condition2     result 
# True               True           True
# True               False          False
# False              True           False
# False              False          False


has_adhar_card = False
has_driving_license = True
can_mark_vote = has_adhar_card or has_driving_license or has_voter_id
print(can_mark_vote) # True
print(not can_mark_vote) # False


#condition1         condition2     result 
# True               True           True
# True               False          False
# False              True           False
# False              False          False


#n1 = int(input("Enter first number:\t "))
#n2 = int(input("Enter second number:\t "))

# print(n)
# print(type(n))
# print(n1>n2)


print(bool(False)) # False
print(bool(True)) # True
print(bool(0)) # False
print(bool(1)) # True
print(bool("")) # False
print(bool("Hello")) # True
print(bool([])) # False
print(bool([1, 2, 3])) # True
print(bool(None)) # False
print(bool(1000)) # True
print("hello" and "ajith")   # True
print(0 and "ajith") # 0
print([1] or "hello") # [1]



print("python" in "python programming") # True
print("java" in "python programming") # False
print("python" not in "python programming") # False
print("java" not in "python programming") # True


a = [1,2,3]
b = [1,2,3]
print(a is b) # False
print(a == b) # True
m = 1
n = 1
print(m is n) # True
print(id(m)) 
print(id(n))  
print(id(a)) 
print(id(b))


#bitwise Operators


# 8   4   2   1
# 1   0   1   0 
# 1   1   0   1
# 1   0   0   0
# 1   0   1   0
# 0   0   1   1

# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1


# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1



#bitwise AND

print(5 & 3) # 1


#bitwise OR

print(5 | 3) # 7


# 0  1  0  1
# 0  0  1  1
# ------------
#  0  0  0  0


# bitwise XOR

# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

print(5 ^ 3) # 6

# bitwise NOT

# 0 = 1
# 1 = 0
#  ~n = -(n+1)

print(~5) # -6

# ~n = -(n+1)
# -8+1=-7
#-7*-1=7

print(~-8) # 7










