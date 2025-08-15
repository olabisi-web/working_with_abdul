# Task1
# Creating a Student Biodata
# Using input to collect name, age, gender, course
# I will then store in dictionart using {} : ,
# print the output : f-string ,{} , :  [] \t, \n
student_name = input("Enter your full name here: ")
student_age = input("Type in your age here: ")
student_gender = input("Enter your gender here: ")
student_course = input("What courses did your offer: ")   
student = {
    "Name": student_name,
    "Age": student_age,
    "Gender": student_gender,
    "Course": student_course,
}
print(f"Name:\t{student_name}\nAge:\t{student_age}\nGender:\t{student_gender}\nCourse:\t{[student_course]}")


