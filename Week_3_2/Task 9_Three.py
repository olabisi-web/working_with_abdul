# Comment the code below appropriately, and using doctring, explain what the code is doing.
# Adapt the code to the case below.
# Federal Government Scholarship Key Eligibility Requirements:
# Citizenship:
# Applicant must be a citizen of Nigeria. 
# Enrollment:
# Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
# Other Scholarships:
# Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
# Academic Qualification:
# For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.


while True:
    name = input("Enter your Full name: ").title()
    if name == 'Stop':
        print("End pf Registration")
        break
    citizenship = input("Enter your Nationality: ").title()
    enrollment = input("Are you a full-time undergraduate in Nigerian university? ").title()
    other_scholarship = input("Are you a beneficiary of any oil and gas schlarship? ").title()
    academic_qualification = input("Do you have 5 distinctions in relevant subject WAEC subject including Mathematics and English? ").title
    

    if citizenship == "Nigerian":
        if enrollment == "Yes":
            if academic_qualification == "Yes":
                if other_scholarship == "No":
                    print(f"{name}, you are eligible for this scholarship")
                else:
                    print(f"{name}, you are not eligible.")

