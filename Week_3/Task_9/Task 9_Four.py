# **Task4: Create a Unique Voters Registration System**

# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.


voter_1 = input("Enter your name: ")
voter_2 = input("Enter your name: ")
voter_3 = input("Enter your name: ")
voter_4 = input("Enter your name: ")
voter_5 = input("Enter your name: ")
voter_6 = input("Enter your name: ")
# store voters name in set.
voters = set()

for voter in [voter_1, voter_2, voter_3, voter_4, voter_5, voter_6]:
    if voter in voter:
        print(f"\nwarning!!P: {voter} has already registered. ")
    else:
        voters.add(voter)


print("\ntotel number of unique voter: ",len(voter))
print("voter list:","," .join(voter))