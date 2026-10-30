student = {
    "name" : "viki",
    "course" : "python",
    "student_id" : "ig123",
    "age" : 20,
    "hobbies" : ["reading","gaming"]
}

d1 = {}      # empty dictionary 
s1 = set()   # empty set 

print(student)
print(type(student))
print(type(d1))
print(type(s1))
student["course"] = "python programming"
student["full_name"] = "sree"

print(student["name"])
print(student)


"""
   - ordered
   - unindexed
   - allow duplicate for values , key should be unique 
   - values are mutable 
   - keys should be hastable
   - values can be of any type
   

"""

items = student.items()
# for a in student:
#     print(student[a])

# print("name" in student)

# print(student["coursee"])

# print(student.get("coursee"))

# print(student.get("coursee","Not Applicable"))

student.update({"course":"Python Programming"})

student.update({"place":"Kochi"})

student.setdefault("age",25)

student.pop("student_id")

# student.popitem()

# print(student)

print(student.keys())

print(student.values())

print(student.items())

for key,value in items:
    print(f"{key:<10}:{value}")

d2 = dict((("emp_no","7S8649"),("emp_name","Parthiv"),("department","Software")))
print(d2)

copy_std = student.copy()
copy_std["course"]="MERN"
copy_std["hobbies"][0]="Singing"
print(copy_std)
print(student)

