# The Federal Government of Nigeria has set the minimum age for admission int federal tertiary institution 
# For the 2025/2026 academic session, the university of lagos(UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post_UTME screening.

print("Welcome to UNILAG Admision Eligibilityn Checker site for 2025/2026 Academic")
print("\nKindly input the following information to check your eligibility for the admission ")
Name = input("Enter your full name (Surname first): ")
Age = input("Enter your age: ")
Course = input("Enter your coures of interest: ")
Utme = int(input("Enter your jamb score: "))
Waec = input("Do you have at leat five credits in your O'level result (including if you have)")
First_choice = input("Did you choose UNILAG as your first_c`h`oice: ")
Post_utem = int(input(" Enter your post_utme score: "))
Dept_cut_off = int(input("Enter your departmental cut_off_make (200-320): ")) 
eligibilty = (Age >=16) and (Utme>= 200) and (First_choice == "yes" and (Waec))