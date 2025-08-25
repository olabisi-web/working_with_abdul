# *Task5: Store Inventory Update**
# -Create a dictionary called store with items and their available quantities. Example:
# store = {"Cup": 7, "Baby_Baby": 4, "Mentos_Gum": 9}
# -Ask the user to input the item they want to buy (e.g., "Pen").
# -Ask the user to input the quantity they want to purchase.
# -Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# -Print the updated dictionary in this format:
# Before purchase: {'Cup': 7, 'Baby_Food': 4, 'Mentos_Gum': 9}
# After purchase: {'Cup': 7, 'Baby_Food': 1, 'Mentos_Gum': 9}


store = {"Cup": 7, "Baby_Food": 4, "Mentos_gum": 9}
print(f"Before Purchase: {store} ")
Items = input("Enter the items you want to buy: ")
Quantity = int(input("Enter the quantity you want to purchase: "))
if Items in store and store[Items]>= Quantity:
    store[Items] -= Quantity
    
else:
    print("Sorry insufficient quantity. ")





    





