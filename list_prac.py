# 1. Find the Largest Element
numbers = [10, 5, 25, 8, 15]
largest = max(numbers)
print(largest)

# 2. Find the Smallest Element
numbers = [10, 5, 25, 8, 15]
smallest = min(numbers)
print(smallest)

# 3. Find Sum of All Elements
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

# 4. Find Average of Elements
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(average)

# 5. Reverse a List Without Using reverse()
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)

# Logic-Based List

# 1. Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)

# 2. Find Second Largest Number
numbers = [10, 20, 50, 40, 30]
second_largest = sorted(set(numbers))[-2]
print(second_largest)

# 3. Separate Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# 4. Find Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [number for number in list1 if number in list2]
print("Common elements:", common_elements)

# 5. Merge Two Lists Without Duplicates
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_list = list(dict.fromkeys(list1 + list2))
print("Merged list:", merged_list)

# Nested List

 # 1. Sum of All Elements in a Matrix
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
matrix_total = sum(sum(row) for row in matrix)
print("Sum of all elements:", matrix_total)

# 2. Find Largest Element in a Matrix
matrix = [
	[1, 2, 3],
	[10, 5, 6],
	[7, 8, 9],
]
largest_matrix_element = max(max(row) for row in matrix)
print("Largest element in matrix:", largest_matrix_element)