# Task 2
# Comment the code
name = input("Enter your name: ")              # input is use to collect data
age = int(input("Enter your age: "))           # input is use to collect data 
score = int(input("Enter your test score: "))  # input is use to collect data
eligibility = (age < 18) and (score > 70)      # using comparison to show the boolean value of the "eligibility" data
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")     # display the data item and data

# Federal Gvernment Scholarship Key Eligibitity
Citizenship= (input("Are you a citizenship of Nigeria "))
Enrollment = (input("Are you a full_time undergradute student "))
Scholarship = input("Are you currenting receiving any scholarship under oil and gas industry ")
Academic_Qualification = input("Enter your five undergradute courses ")
eligibility = (Citizenship == "yes") and (Enrollment == "yes" and (Scholarship == "no" ) amd (qualification == "yes"))
result = {True: "Congratulations, you are eligible for the 2025 ongoing federal Government Scholarship.", False: "Sorry, you're not eligible for the ongoing Federal Government Scholarship."}
print(f"\nAre you a citizen of Nigria: {Citizenship}\nAre you a full time undergraduate: {Enrollment}\nAre you a beneficiary of an exist")
print(result[eligibility])

