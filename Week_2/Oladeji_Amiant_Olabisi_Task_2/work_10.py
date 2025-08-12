# School Fees Breakdown

name = input("What is your school name?: ")
fee = float(input("How much is the Tuition fee?: "))
Hostel = float(input("How much is the Hostel fee?: "))
feeding = float(input("How much is the feeding fee?: "))
Total_payment = float(fee + Hostel + feeding)
print(f"The Total cost of the school fees is {Total_payment}")

print("\n")
print("*" * 50)
print("\t",        name)
print("\t       RECEIPT")
print("*" * 50)
print("\n")

print(f"Tution fee:\t₦{fee}K\nHostel fee:\t\t₦{Hostel}K\nFeeding fee:\t\t₦{feeding}K\n\nTotal School Fees:\t₦{Total_payment}K")
print("\n")
print("=" * 40)
print("      THANK YOU FOR YOUR PURCHASE")
print("=" * 40)
