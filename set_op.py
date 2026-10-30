"""
set is an unordered collection of unique element 

   -unordered
   -unindexed
   -mutable
   -it does not allow duplicate values 
   
"""

students = {"viki","sree","nidi","gopu"}
n = set()
print(type(n))
students.add("dinu")
# students.remove("gopu")   #remove the element if exists, else generate an error
# students.remove("nidi")
# students.discard("sree")
# students.pop()
# students.clear()
# students.remove('nidhi')
students.add('sudhi')
print(students)
print(len(students))
for student in students:
    print(student)

print(set(["Python", "MERN", "Python", "DS", "DS", "Python"]))
print({"Harish","a",1,True,0,False,45,-89})

movie_set_1 = {"Jailer","Killukkam","CID Moosa","KGF","Vettam"} # A
movie_set_2 = {"Vettam","KGF","Drishyam","Obsession","Parava"} # B

# print(movie_set_1.union(movie_set_2))
# print(movie_set_1 | movie_set_2)
# print(movie_set_1.intersection(movie_set_2))
# print(movie_set_1 & movie_set_2)
# print(movie_set_1.difference(movie_set_2))  # A - B = A - (A&B)   B - A = B - (A&B)
# print(movie_set_1 - movie_set_2)
# print(movie_set_2 - movie_set_1)
# print(movie_set_1.symmetric_difference(movie_set_2)) # A ^ B  (A | B) - (A & B)
# print(movie_set_1 ^ movie_set_2)
# movie_set_1.update(movie_set_2)
# movie_set_1.intersection_update(movie_set_2)
# movie_set_1.difference_update(movie_set_2)

movie_set_1.symmetric_difference_update(movie_set_2)

print(movie_set_1)


print(movie_set_1)

numbers = {1,2,45,78,93,96,73,10,8}
even_numbers = {2,78,96,10,8}
print(numbers.issuperset(even_numbers))
print(even_numbers.issubset(numbers))
print(numbers.isdisjoint(even_numbers))
print({1,5,7}.isdisjoint({2,8,10}))

