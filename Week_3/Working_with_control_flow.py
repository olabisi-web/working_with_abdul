# # Conditional Statement
# # If Statement
# age = 20
# if age >= 18:
#     print("You are eligible to vote")     #You are eligible


# # If-else Statement
# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")     # Insufficient balance

# # if-elif_else statement
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")     # Grade

# # Nestend if 
# # Placing an if inside another if. 
# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")    # You can vote

# # For loop
# # Iterates through each element in a LIST.

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")


# ## Some usecases
# # Iterating through shopping lists.

# # Checking availability of products.

# # Displaying student names, etc.    # I like apple, # I like banana, # I like orange

# # Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

# coordinates = (0.34654, -0.48585, 0.57477)
# for point in coordinates:
#     print(f"Point: {point}")

# ## Some usecases
# # Storing fixed sensor readings.
# # Displaying fixed seating positions, etc.   # Point: 0.34654 # Point: -0.48585 #   Point: 0.57477

# # Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# ## Some usecases

# # Reading database records.

# # Showing user profile details.

# # Checking configuration settings, etc.    # name: Tunde # age: 16 # grade: A

# # Iterates through each element in a STRING. Remember that strings are sequences of characters.

# word = "PYTHON"
# for char in word:
#     print(char)

# ## Some usecases

# # Counting vowels/consonants.

# # Password validation (checking digits/special chars).

# # Text analysis, etc.      # P, # Y, # T, # H, # O, # N

# # While loop
# # Using while loop

# ## Documenting my thoughts##
# # Let the loop start with count = 1
# # Let it keep printing until count is greater than 5
# # Let the loop terminate when the condition is no longer true

# ## My code
# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1      # Number: 1, # Number: 2, # Number: 3, # Number: 4, # Number:5

# # Incrementing with `while`

# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1    # 1 2 3 4 5 6 7 8 9 10
# # Decrementing with `while`

# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -= 1    # Countdown: 10, # Countdown: 9 # Countdown: 8 # Countdown: 7 # Countdown: 6 # Countdown: 5 # Countdown: 4 # Countdown: 3 # Countdown: 2 # Countdown: 1
# # While with User Input
# ## Keep asking until the user enters a correct password.

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted!")    # Abdul

# Understanding while True
# Keep asking the user for a name until they type "exit".

while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# ---> I used `break` here. If you dont know what it is or what it is doing, its OK. I will explain it next...

## Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.
# Breat 
for num in range(1, 10):
    if num == 5:
        break
    print(num)

#The loop stops completely when num == 5.

# Stop searching when an item is found.

# Exit when user input matches a condition.

# Prevent unnecessary iterations
# Continue
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 3 is skipped, but the loop continues.

## Some usecases

#Skip invalid data.

#Ignore unwanted characters (like spaces in a string).

# Continue running but avoid certain cases, etc.
# Pass
for num in range(1, 6):
    if num == 3:
        pass   # do nothing for now
    else:
        print(num)

# At num == 3, Python executes pass (nothing happens).

## Some usecases

# Writing code structure (to fill in later).

# Placeholders in class/method definitions.

# Temporarily disable parts of code
# Let try while True again
# Try and think through this...

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")   # Menu: 1. Say Hello # 2. Say Goodbye # 3. Exit
# Try and use while True for validation

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")       
# LEets make a guess

secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")     
# Do you remember this?

balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")               