# . Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.


# Task1_9
# USSD_CODe
balance = 25000
# Welcome_to_Nigerian_Bank = input("Welcome to Nigerian bank: ")
print("Welcome to Nigerian bank you can do all your transaction here")
# Else:
Ussd_code = input("Enter your ussd_code: ")
print(f"your ussd_code is: {Ussd_code}")
while True:
    print("\nAccount Menu:")
    print("1. Check account balance")
    print("2. Buy airtime")
    print("3. Buy data")
    choice = input("Enter your choice here:")
    if choice == "1":
         print(f"your account balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter amount of airtime: "))
        if amount <= balance:    
         print(f"airtime successful. New balance: {balance}")
    elif choice == "3":
        amount = int(input("Enter amount of data: "))
        print(f"data successful. New balance: {balance}")   
    else:
       print ("Thank you for using our ATM. Goodbye!")    

