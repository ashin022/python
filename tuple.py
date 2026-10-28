# tuple is a collection of hetrogenous data.
# -ordered
# -indexed
# -allow duplicates
# -Immutable


t1 =(1,2,3,4,5)
print(t1)
print(type(t1))
t2 = 45,56,78,72
print(t2)
print(type(t2))
a,b,c = (1,2,3)  # unpacking

for x in t1:
    print(x)

print(len(t1))
print(1 in t1)
print(t1[0])


print(t1[:-2])
print(t1[2:])
print(t1[::2])


number = [78,96,77,36,10,2,75,34]

for index,value in enumerate(number):
    print(f"index:{index} \tvalue:{value}")
