# Student Record

# Crate an empty dictionary call student
Student = {}
name = input("Enter student name: ")
age = input("Enter student age: ")

# Ask the user to input thir name and age, then store them in the dictionary.
student = {
    "Name": name,
    "Age": age,
}
print(student)

# Add a list of scores (e.g., [70,80,90]) to the dictionary.
scores = [70,85,90]
print(scores)

# Cheak if the student has passed (average score >=50). Save the result (True/False) in the dictionary under the key "passed".
# Average_score = sum(scores) / len(scores)
average_score = (70, 85, 90)/3
print(average_score >= 50)   # True (passed)
passed = (average_score >= 50)

# Check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
student['teenager' ] = 13 <= int(age) <= 19
print("student:, teenager")

# Print out the complete record in the format:
print(f"Student Name: {name}\nAge: {age}\nScores: {scores}\nPassed: {student['passed']}\nTeenager: {'teenager'}")
