#Problem 1 
print("Problem 1: Array Creation and Basic Operations")
print("Part A: Create Arrays")
#1
from itertools import product
import numpy as np
zero_arr = np.zeros(8)
print("Zero Array:", zero_arr)
#2
ones_matrix = np.ones((3, 4))
print(f"Ones Matrix: \n {ones_matrix}")
#3
range_arr = np.arange(10, 51, 5)
print("Range Array:", range_arr)
#4 
linear_arr = np.linspace(0, 2, 9)
print("Linear Array:", linear_arr)

print("Part B: Basic Operations")
a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])
#1
print(a+b)
#2
print(a*b)
#3
print(a**b)
#4
print(a/b)
#5
print(np.sum(a))
#6
print(np.sum(b))

#Problem 2
print("Problem 2: Array Attributes and Statistics")
print("Part A: Array Attributes")
num_matrix = np.arange(1, 21).reshape(4,5) 
#1
print(num_matrix)
#2
print("Shape:", num_matrix.shape)
#3
print("Dimensions:", num_matrix.ndim)
#4
print("Number of Elements:", num_matrix.size)
#5
print("Data Type:", num_matrix.dtype)
#6
print("Memory Size (bytes):", num_matrix.nbytes)

#Part B:Statistics
#1
print("Mean:", np.mean(num_matrix))
#2
print("Standard Deviation:", np.std(num_matrix))
#3
print("Minimum:", np.min(num_matrix))
print("Maximum:", np.max(num_matrix))
#4
print("Sum of each row:", np.sum(num_matrix, axis=1))
#5
print("Sum of each column:", np.sum(num_matrix, axis=0))
#6
print("Index of maximum:", np.argmax(num_matrix))

#Problem 3: Indexing and boolean selection
print("Problem 3: Indexing and Boolean Selection")
# Student scores: 6 students, 4 exams
scores = np.array([
[85, 90, 78, 92], # Alice
[70, 65, 72, 68], # Bob
[95, 98, 94, 97], # Carol
[60, 55, 58, 62], # Dave
[88, 85, 90, 87], # Eve
[75, 80, 77, 82] # Frank
])
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']
print("Part A: Basic Indexing")
#1 Carols exam 2 score
print("Carol's Exam 2 Score:", scores[2, 1])
#2
print("Alice's scores:", scores[0])
#3
print("All students' Exam 3 scores:", scores[:, 2])
#4 2x2 sumb matrix of bob and carols scores for exam 1 and 2
print("Bob and Carol's scores for Exam 1 and 2:\n", scores[1:3, 0:2])

#Part B: Boolean Selection
print("Part B: Boolean Selection")
#1
mask = scores >= 90
print("All scores >= 90:", scores[mask])
print("Count of scores >= 90:", np.sum(mask))
#2
print("All scores >= 90:", scores[scores >= 90])
#3
print("Count of scores >= 90:", np.sum(scores >= 90))
#4
avg_scores = np.mean(scores, axis=1)
student_names = np.array(students)[avg_scores >= 85]
print("Students with average score >= 85:", student_names)
#5
scores[scores < 60] = 60
print("Modified array with failing scores replaced with 60:")
print(scores)

#Problem 4: Reshaping and broadcasting
print("Problem 4: Reshaping and Broadcasting")
print("Part A: Reshaping")
#1 
arr_1d = np.arange(1, 25)
print("1D Array:", arr_1d)
#2
arr_4x6 = arr_1d.reshape(4, 6)
print("4x6 Matrix:\n", arr_4x6)
#3
arr_2x3x4 = arr_1d.reshape(2, 3, 4)
print("2x3x4 3D Array:\n", arr_2x3x4)
#4
arr_flattened = arr_2x3x4.flatten()
print("Flattened Array:", arr_flattened)

print("Part B: Broadcasting") 
# Rows: products (Apple, Banana, Orange)
# Columns: stores (Store1, Store2, Store3, Store4)
prices = np.array([
[1.20, 1.50, 1.30, 1.40], # Apple
[0.50, 0.60, 0.55, 0.45], # Banana
[0.80, 0.90, 0.85, 0.75] # Orange
])
#1 
discounted_prices = prices * 0.9
print("Discounted Prices:\n", discounted_prices)
#2
delivery_fee = np.array([0.10, 0.10, 0.10, 0.10])
final_prices_with_fee = discounted_prices + delivery_fee
print("Final Prices with Delivery Fee:\n", final_prices_with_fee)
#3
tax_rates = np.array([0.08, 0.06, 0.07, 0.05])
final_prices_with_tax = final_prices_with_fee * (1 + tax_rates)
print("Final Prices with Tax:\n", final_prices_with_tax)
#4
mean_prices = np.mean(prices, axis=1, keepdims=True)
normalized_prices = prices - mean_prices
print("Normalized Prices:\n", normalized_prices)