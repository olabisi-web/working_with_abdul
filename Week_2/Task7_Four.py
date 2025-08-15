# Creating a unique members registration
# Collect the name using input()
# Define the name that conjoin 
# Convert to set {} or ()
# Dictionary k-v pairing name as key and length len() as values
User_name = input("Enter 3 of your name: ").split()
converted_User_name = set(User_name)
members_reg = {User_name: len(user_name) for user_name in converted_User_name }
print(members_reg)


