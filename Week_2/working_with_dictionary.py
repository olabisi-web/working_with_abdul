# #Creating Dictionaries

# # 1. Using curly braces
# student = {
#     "name": "Ade",
#     "age": 20,
#     "course": "Computer Science"
# } 
# print(student)

# # 2. Using the dict() constructor
# student_info = dict(name="John", age=25, course="Maths")
# print(student_info)

# # 3. Empty dictionary
# empty_dict = {}
# print(empty_dict)

# #Dictionary Comprehension

# # Create a dictionary of numbers and their squares
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# # With Condition

# # # Dictionary of even numbers and their cubes
# evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
# print(evens_cube) 
# even_cube = {x: x**3 for x in range(10, 20) if x % 4 == 0}
# print(even_cube)
 #  From Existing Dictionary

# students = {"Ada": 85, "John": 40, "Musa": 65}

# # Filter students who passed (score >= 50)

# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)

# Using String Keys

# names = ["Ada", "John", "Musa"]
# lengths = {name: len(name) for name in names}
# print(lengths)
# names = ["Opeyemi", "Temi", "AbdulRaheem"]
# lengths = {name: len(name) for name in names}
# print(lengths)

# Accessing Dictionary Items
# Define a dictionary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# print(student["name"])
# print(student.get("age"))
# print(student.get("course"))
# Removing Item from Dictionaries
# 1.  Using pop()
# student.pop("course")
# print(student.pop("course"))
# 2. Using popitem() - removes last inserted key-value
# student.popitem()

# 3. Using del keyword
# del student["course"]

# 4. Using clear() - removes all items
# student.clear()

# print(student)

# Dictionary Methods
# person = {"name": "Emeka", "age": 30}

# 1. keys()
# print(person.keys())

# 2. values()
# print(person.values())
# 3. items()
# print(person.items())
# 4. update()
# person.update({"age": 31, "city": "Lagos"})
# print(person)

# Nested Dictionaries
#students = {
#   "student1": {"name": "Ada", "age": 20},
#    "student2": {"name": "John", "age": 22}
# }
# print(students["student1"]["name"])  # Access nested data

# Looping Through Dictionaries
# Define a dictionary
#student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# Loop through keys
# for key in student:
#    print(key)
# Loop through keys
# Loop through values
# for value in student.values():
#     print(value)
# Loop through key-value pairs
# for key, value in student.items():
#     print(f"{key}: {vaiue}")
# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")

students = [
    {"Name": "John", "Interest": "AI", "TRACK": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_EEV"}
]

print(students[0]["Name"])
print(students[1]["Track"])

students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1]) 