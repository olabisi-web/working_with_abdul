# Method 1: Using square brackets
empty_list = []
print(empty_list) # Output: []

# Method 2: Using the list() constructor 
empty_list2 = list()
print(empty_list2) # Output: []

# List of integers
numbers = [1, 2,3,4,5]
print(numbers) # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list) # Output: ['Alice', 25, 5.8,]

# From a strint (each character becomes an element)
chars = list("hello")
print(chars) # Output: ['h', 'e', 'l', 'l', 'o']


# Squares of number 0-4
squares = [x**2 for x in range(5)]
print(squares) # output: [0, 1, 4, 9, 16]

# Even number between 10-20
evens = [x for x in range(21) if x % 2 == 0]
print(evens) # Output: [10, 12, 14, 16, 18, 20]

# Matrix-list
matrix = [[11, 12], [13, 14], [15, 16]]
print(matrix) # Output: [[11, 12], [13, 14], [15, 16]]

# Matrix-list 
matrix = [[4, 6], [8, 10]]
print(matrix) #Output: [[4. 6]], [8, 10]]


# Accessing elements in a nested list 
print(matrix[0])     # Output: [1, 2]
print(matrix[0][1])  # Output:2


fruits = ["mango","orange", "banana"]
print(fruits)      # ['mango', 'orange', 'banana']
print(fruits[0])   # mango (first element)
print(fruits[2])   # banana (third element)


items = ["rice", "beans", "yam", "rice"]
print(items) # ['rice', beans', yam', rice']

name = "bisi"
print(name)