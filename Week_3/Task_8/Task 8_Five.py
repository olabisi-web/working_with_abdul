# Store Inventory Update
# Create a dictionary called store with items and their available  quantities. Example: store = {"Book": 10, "Pen": 20, "Bag": 5}
# Available items
items = ["Cloth", "Ball", "Fan", "Baby diapers"]
# Quantity of each item
qty = [500, 100, 150, 200]
print("The quantity of each available item are: ")
store = {items[0]: qty[0], items[1]: qty[1], items[2]: qty[2], items[3]: qty[3] }
print(store)
before_purchase = {items: qty for item, qty in store.items()}

# Ask the user to input the item they want to buy (e.g.,"Pen".)
Purchase = input("\nEnter the item you want to buy from the store: ")

# Ask the user to input the quantity they want to purchase.
Quantity = input("Enter the quantity of item you want to buy from the store: ")

# Use the assignment operator -= to update(reduce)the item quantity in the dictionary.
store[Purchase] -= Quantity
print(store)

# Print the updated dictionary in this format:
print(f"Before purchase: {store}\nAfter purchase: (after_purchase) ")


