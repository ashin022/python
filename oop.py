# class classname:
   # attributes
   # methods    
   # pass

#clss childclass(parentclass):derived , sub , child
#pass 

# class person:
#     pass 

# class student:
#     #   college = "iggis"  # class variable
#     def __init__(self, name, rollno,marks):  # constructor
#         self.name = name  # instance variable
#         self.rollno = rollno  # instance variable
#         self.marks = marks  # instance variable
#         self.attendance = False  # instance variable
        
#     def mark_attendance(self, is_present):  # instance method
#         self.attendance = is_present 
#     def student_details(self):  # instance method
#        print(f"name:{self.name}")
#        print(f"rollno:{self.rollno}")
#        print(f"marks:{self.marks}")

    # def attendance(self,is_present):  # instance method
    #     print(f"student is {'present' if is_present else 'absent'}")

# std1 = student()  # object creation
# std2 = student()  # object creation
# std2.college = "kmp "  # instance variable
# print(std1.college)  # access class variable
# print(std2.college)  # access instance variable

# print(std1)
# print(std2)
# print(type(std1))
# print(type(std2))

# std1.attendance(True)  # calling instance method
# std2.attendance(False)  # calling instance method

# std1 = student("viki", 1, 90)  # object creation
# std2 = student("sree", 2, 80)  # object creation
# std1.name = "viki m "  # instance variable

# print(std1.name)  # access instance variable
# print(std2.name)  # access instance variable
# std1.mark_attendance(True)  # calling instance method
# std1.student_details()  # calling instance method


# class person:
#     def __init__(self, name, age):
#         print("init in person class")
#         self.name = name
#         self.age = age
#     def details(self):
#         print("self")
#         print(f"name:{self.name}")
#         print(f"age:{self.age}")    
# class student(person):
#     def __init__(self, name, age, rollno, marks):
#         print("init in student class")
#         super().__init__(name, age)  # calling parent class constructor
#         self.rollno = rollno
#         self.marks = marks  # instance variable
   
#     def student_details(self):
#         super().details()  # calling parent class method
#         print(f"name:{self.name}")
#         print(f"age:{self.age}")
#         print(f"rollno:{self.rollno}")
#         print(f"marks:{self.marks}")     



# std1 = student("viki", 20, 1, 90)  # object creation

# print(std1.name)  # access instance variable

# std1.details()  # calling instance method



# abstract class: class which contains atleast one abstract method

import math
from abc import ABC, abstractmethod


# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         ...

#  class circle(shape):
#     def area(self,r):
#         print(math.pi*r*r)
        

# # c1 = circle()
# c1.area(5)

import random
user = input("Enter your choice : ")
computer = random.choice(["rock", "paper", "scissors"])
print(f"Computer choice: {computer}")
