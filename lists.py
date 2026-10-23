'''
list is a collection of heterogenous data

 - ordered 
 - indexed
 - allow duplicates
 - mutable
 
'''

number = [78,96,77,36,10,2,25,34]
print(number)
print(type(number))
print(len(number))
print(number[6])
print(number[-1])
print(number[1:6])
print(number[-7:-2])
print(number[:-2])
print(number[4:])
print(number[::2])
print(number[::-3])
print(number[::-7])
print(number[0])
number[4]=100
number.append(845)
number.append(8)
number.insert(5,23)
# number.extend("fhgd")
number.extend([10,20,30])


print(number)
even_count = 0
for n in number:
    if n % 2 == 0:
        even_count += 1

print(even_count) 

# number.pop()
# number.remove(100)
# del number[7]
# number.clear()

l2 =[]
l3 = list(number)
print(number)
print(l3) # ("k,"a","r......")
print(l3 is number)

print(number.count(77))
print(number.index(100))
print(22 in number)
print(22 not in number)


l4 = number.copy()

l4[1]="viki"
print(l4)
print(number)
print(l4 is number)
#number.sort(reverse=true)
number.reverse()
print(number)

l5 = [[12,13,14],[22,33,44],[100,200,300]]
print(l5[1][2])
l6 = l5.copy() # shallow copy
l6[1][2] = 555
print(l5)
print(l6)

# for x in l5:
#     for n in x:
#         print(n)